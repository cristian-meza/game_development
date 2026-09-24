import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

sp.init_printing()

# PROBLEM 1 - Orthogonal trajectories

print("\n" + "=" * 65)
print("PROBLEM 1")
print("=" * 65)

x = sp.symbols("x", positive=True)
a = sp.symbols("a", real=True)
f = sp.Function("f")

family_expr = a * sp.exp(-x**2)

# 1(a)

print("\n1(a)")

# At an intersection point, f(x) = a*e^(-x^2).
intersection_eq = sp.Eq(f(x), family_expr)
a_of_x = sp.solve(intersection_eq, a)[0]

print("At an intersection point:")
sp.pprint(intersection_eq)
print("\nSolving for a gives:")
sp.pprint(sp.Eq(a, a_of_x))

# 1(b)

print("\n1(b)")

# Parametric tangent vector for the orthogonal trajectory (x, f(x))
tangent_orth = sp.Matrix([1, sp.diff(f(x), x)])

# Parametric tangent vector for a family curve (x, a*e^(-x^2))
tangent_family = sp.Matrix([1, sp.diff(family_expr, x)])

# Orthogonal tangent vectors have dot product 0.
dot_product = sp.simplify(tangent_orth.dot(tangent_family))
dot_at_intersection = sp.simplify(dot_product.subs(a, a_of_x))

print("Tangent vector to y = f(x):")
sp.pprint(tangent_orth)
print("\nTangent vector to y = a*e^(-x^2):")
sp.pprint(tangent_family)
print("\nDot product after substituting the value of a from part (a):")
sp.pprint(dot_at_intersection)

orthogonality_eq = sp.Eq(dot_at_intersection, 0)
print("\nDifferential equation from orthogonality:")
sp.pprint(orthogonality_eq)

# Solve the equation for f'(x); this form is convenient for dsolve.
fprime_rhs = sp.solve(orthogonality_eq, sp.diff(f(x), x))[0]
ode = sp.Eq(sp.diff(f(x), x), fprime_rhs)
print("\nEquivalent solved form:")
sp.pprint(ode)

# 1(c)

print("\n1(c)")
print(
    "By hand: start with 1 - 2*x*f(x)*f'(x) = 0. "
    "Rearrange to 2*f(x)*f'(x) = 1/x. Since the left side "
    "is d/dx[(f(x))^2], integrate both sides to get "
    "(f(x))^2 = ln|x| + C, so f(x) = +/-sqrt(ln|x| + C)."
)

print("\nSymPy general solution:")
general_solution = sp.dsolve(ode)
for sol in general_solution if isinstance(general_solution, list) else [general_solution]:
    sp.pprint(sol)

# 1(d)

print("\n1(d)")
print("Plotting the seven orthogonal trajectories in red and family curves in blue.")

initial_points = [
    (sp.Rational(1, 2), sp.Rational(1, 2)),
    (sp.Rational(1, 2), sp.Rational(1, 1)),
    (sp.Rational(1, 2), sp.Rational(3, 2)),
    (sp.Rational(1, 2), sp.Rational(2, 1)),
    (sp.Rational(1, 2), sp.Rational(5, 2)),
    (sp.Rational(1, 2), sp.Rational(3, 1)),
    (sp.Rational(1, 2), sp.Rational(7, 2)),
]

# x=0 cannot be inserted into log(x), so start just to the right of 0.
x_values = np.linspace(1e-4, 4, 2500)

plt.figure(figsize=(7, 7))

for i, (x0, y0) in enumerate(initial_points):
    # Requirement: use dsolve with an initial condition.
    orth_solution = sp.dsolve(ode, ics={f(x0): y0})
    orth_expr = orth_solution.rhs

    # Find the member of y=a*e^(-x^2) through (x0,y0).
    a_value = sp.solve(sp.Eq(y0, family_expr.subs(x, x0)), a)[0]
    family_through_point = sp.simplify(family_expr.subs(a, a_value))

    orth_func = sp.lambdify(x, orth_expr, "numpy")
    family_func = sp.lambdify(x, family_through_point, "numpy")

    with np.errstate(invalid="ignore", divide="ignore"):
        orth_y = np.asarray(orth_func(x_values), dtype=float)
        family_y = np.asarray(family_func(x_values), dtype=float)

    plt.plot(
        x_values,
        orth_y,
        color="red",
        label="Orthogonal trajectories" if i == 0 else None,
    )
    plt.plot(
        x_values,
        family_y,
        color="blue",
        label="Original family" if i == 0 else None,
    )

plt.xlim(0, 4)
plt.ylim(0, 4)
plt.gca().set_aspect("equal", adjustable="box")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Problem 1(d): Orthogonal Trajectories")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.show()

# PROBLEM 2 - Forward Euler method
# IVP: y' = (y+t)/(1+t), y(0) = -1/2

print("\n" + "=" * 65)
print("PROBLEM 2")
print("=" * 65)

t, y = sp.symbols("t y", real=True)
F = (y + t) / (1 + t)

# 2(a)

print("\n2(a)")
print("Plotting a 21 by 21 direction field on [-1,3] x [-1,3].")
print("Note: the differential equation is singular at t = -1; the point (-1,1) is undefined.")

# 21 evenly spaced values including both boundaries.
t_grid = np.linspace(-1, 3, 21)
y_grid = np.linspace(-1, 3, 21)
T, Y = np.meshgrid(t_grid, y_grid)

# A tangent vector with slope (y+t)/(1+t) is proportional to
# (1+t, y+t). This avoids direct division by zero at t=-1.
U = 1 + T
V = Y + T
length = np.sqrt(U**2 + V**2)

U_normalized = np.divide(U, length, out=np.zeros_like(U), where=length != 0)
V_normalized = np.divide(V, length, out=np.zeros_like(V), where=length != 0)

plt.figure(figsize=(7, 7))
plt.quiver(T, Y, U_normalized, V_normalized, angles="xy", pivot="mid")
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Problem 2(a): Direction Field")
plt.grid(True, alpha=0.25)
plt.tight_layout()
plt.show()

# 2(b)
# ----------------------------
print("\n2(b)")

h_sym = sp.Rational(1, 10)
t0_sym = sp.Integer(0)
y0_sym = -sp.Rational(1, 2)

# Use .subs() as requested in the assignment.
slope0 = sp.simplify(F.subs({t: t0_sym, y: y0_sym}))
y1_sym = sp.simplify(y0_sym + h_sym * slope0)

print("Slope at (0, -1/2):")
sp.pprint(slope0)
print("Approximation for y(0.1):")
sp.pprint(y1_sym)
print("Decimal:", float(y1_sym))

# 2(c)

print("\n2(c)")

first_four = [y0_sym]
for i in range(3):
    ti = sp.Rational(i, 10)
    yi = first_four[-1]
    slope_i = sp.simplify(F.subs({t: ti, y: yi}))
    next_y = sp.simplify(yi + h_sym * slope_i)
    first_four.append(next_y)

print("Array [y(0), approx y(0.1), approx y(0.2), approx y(0.3)]:")
sp.pprint(first_four)
print("Decimal form:")
print(np.array([float(value) for value in first_four]))

# 2(d)

print("\n2(d)")

h = 0.1
A = np.zeros(31)
A[0] = -0.5

for i in range(1, 31):
    t_previous = (i - 1) * h
    y_previous = A[i - 1]
    slope = float(F.subs({t: t_previous, y: y_previous}))
    A[i] = y_previous + h * slope

print("Euler array A with 31 values:")
print(np.array2string(A, precision=8, separator=", "))

# ----------------------------
# 2(e)
# ----------------------------
print("\n2(e)")

Yfun = sp.Function("y")
ivp = sp.Eq(sp.diff(Yfun(t), t), (Yfun(t) + t) / (1 + t))
exact_solution = sp.dsolve(ivp, ics={Yfun(0): -sp.Rational(1, 2)})

print("Exact solution of the IVP:")
sp.pprint(exact_solution)

exact_func = sp.lambdify(t, exact_solution.rhs, "numpy")
t_exact = np.linspace(0, 3, 1000)
t_euler_01 = np.linspace(0, 3, 31)

plt.figure(figsize=(8, 5))
plt.plot(t_exact, exact_func(t_exact), label="Exact solution")
plt.plot(t_euler_01, A, marker="o", markersize=3, label="Euler, h = 0.1")
plt.xlim(0, 3)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Problem 2(e): Exact Solution vs. Euler Approximation")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.show()

# 2(f)

print("\n2(f)")

h_fine = 0.01
B = np.zeros(301)
B[0] = -0.5

for i in range(1, 301):
    t_previous = (i - 1) * h_fine
    y_previous = B[i - 1]
    slope = float(F.subs({t: t_previous, y: y_previous}))
    B[i] = y_previous + h_fine * slope

t_euler_001 = np.linspace(0, 3, 301)

plt.figure(figsize=(8, 5))
plt.plot(t_exact, exact_func(t_exact), label="Exact solution")
plt.plot(t_euler_001, B, label="Euler, h = 0.01")
plt.xlim(0, 3)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Problem 2(f): Exact Solution vs. Euler Approximation, h = 0.01")
plt.grid(True, alpha=0.25)
plt.legend()
plt.tight_layout()
plt.show()

# Compare the numerical errors for the two step sizes.
exact_on_01 = exact_func(t_euler_01)
exact_on_001 = exact_func(t_euler_001)
max_error_01 = np.max(np.abs(A - exact_on_01))
max_error_001 = np.max(np.abs(B - exact_on_001))

print("Maximum error with h = 0.1 :", max_error_01)
print("Maximum error with h = 0.01:", max_error_001)
print(
    "Observation: with the smaller step size h = 0.01, the Euler approximation "
    "lies much closer to the exact solution. Using more, smaller steps reduces "
    "the accumulated approximation error."
)
