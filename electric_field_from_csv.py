import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_voltage_csv(filename):
    """Load a CSV containing only voltage values arranged as a rectangular grid."""
    voltage = np.genfromtxt(filename, delimiter=",")

    if voltage.ndim != 2:
        raise ValueError("The CSV must contain a 2-D rectangular grid of voltage values.")

    if np.isnan(voltage).any():
        raise ValueError(
            "The CSV contains blank or non-numeric cells. "
            "Remove headers/labels and make sure every grid cell contains a voltage value."
        )

    if voltage.shape[0] < 2 or voltage.shape[1] < 2:
        raise ValueError("The voltage grid must contain at least 2 rows and 2 columns.")

    return voltage


def compute_electric_field(voltage, dx=1.0, dy=1.0):
    """
    Compute E = -grad(V).

    Spreadsheet convention:
        A1 is the top-left corner.
        Columns move to the right (+x).
        Rows move downward in the file, while physical +y is upward.

    dx and dy are the physical distances between neighboring measurements.
    For example, if points are 1 cm apart, use dx = dy = 0.01 meters.
    """
    rows, cols = voltage.shape

    x = np.arange(cols) * dx

    # Row 0 (A1 row) is the TOP of the rectangle, so its physical y value
    # should be the largest. This keeps +y pointing upward.
    y = (rows - 1 - np.arange(rows)) * dy

    # np.gradient can use the actual coordinate arrays, including decreasing y.
    dV_dy, dV_dx = np.gradient(voltage, y, x)

    Ex = -dV_dx
    Ey = -dV_dy
    magnitude = np.hypot(Ex, Ey)

    return x, y, Ex, Ey, magnitude


def plot_field(voltage, x, y, Ex, Ey, magnitude, stride=1, title=None):
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))

    # Voltage background / equipotential contours
    contour = ax.contourf(X, Y, voltage, levels=25, cmap="coolwarm")
    voltage_bar = fig.colorbar(contour, ax=ax, pad=0.02)
    voltage_bar.set_label("Electric potential V (volts)")

    # Plot a subset of arrows if stride > 1 to reduce clutter.
    s = max(1, stride)
    q = ax.quiver(
        X[::s, ::s],
        Y[::s, ::s],
        Ex[::s, ::s],
        Ey[::s, ::s],
        magnitude[::s, ::s],
        cmap="viridis",
        pivot="mid",
    )

    field_bar = fig.colorbar(q, ax=ax, pad=0.08)
    field_bar.set_label("|E| (volts per distance unit)")

    ax.set_xlabel("x position")
    ax.set_ylabel("y position")
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title or "Electric Field from Measured Electric Potential")
    ax.grid(alpha=0.2)

    # A1 corresponds to x = 0 and the maximum y value (top-left).
    ax.scatter([x[0]], [y[0]], marker="s", s=45, label="A1 (top-left)")
    ax.legend(loc="best")

    plt.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Compute and plot electric-field vectors from a rectangular CSV voltage grid."
    )
    parser.add_argument("csv_file", help="CSV file containing the voltage grid")
    parser.add_argument(
        "--dx",
        type=float,
        default=1.0,
        help="Horizontal spacing between adjacent voltage measurements (default: 1.0)",
    )
    parser.add_argument(
        "--dy",
        type=float,
        default=1.0,
        help="Vertical spacing between adjacent voltage measurements (default: 1.0)",
    )
    parser.add_argument(
        "--stride",
        type=int,
        default=1,
        help="Plot every Nth electric-field arrow to reduce clutter (default: 1)",
    )

    args = parser.parse_args()

    if args.dx <= 0 or args.dy <= 0:
        raise ValueError("dx and dy must be positive.")
    if args.stride < 1:
        raise ValueError("stride must be at least 1.")

    voltage = load_voltage_csv(args.csv_file)
    x, y, Ex, Ey, magnitude = compute_electric_field(voltage, args.dx, args.dy)

    print(f"Loaded grid: {voltage.shape[0]} rows x {voltage.shape[1]} columns")
    print(f"Minimum voltage: {voltage.min():.6g} V")
    print(f"Maximum voltage: {voltage.max():.6g} V")
    print(f"Maximum electric-field magnitude: {magnitude.max():.6g}")

    plot_field(
        voltage,
        x,
        y,
        Ex,
        Ey,
        magnitude,
        stride=args.stride,
        title=f"Electric Field — {Path(args.csv_file).name}",
    )


if __name__ == "__main__":
    main()
