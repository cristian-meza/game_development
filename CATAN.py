import random
import pygame
pygame.init()
screen = pygame.display.set_mode((900, 900)) 
run = True
resources = ["robber", "wood", "wood", "wood", "wood", "ore", "ore", "ore", "sheep", "sheep", "sheep", "sheep", "hay", "hay", "hay", "hay", "brick", "brick", "brick"]
numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
pairs = []
tile = 900/28
differences = ((8*tile,6*tile), (12*tile,6*tile), (16*tile,6*tile)   ,   (6*tile,9*tile), (10*tile,9*tile), (14*tile,9*tile), (18*tile,9*tile)   ,   (4*tile,12*tile), (8*tile,12*tile), (12*tile,12*tile), (16*tile,12*tile), (20*tile,12*tile)   ,   (6*tile,15*tile), (10*tile,15*tile), (14*tile,15*tile), (18*tile,15*tile)   ,   (8*tile,18*tile), (12*tile,18*tile), (16*tile,18*tile)) 
di = 0
num_font = pygame.font.SysFont(None, 50)
for i in range(19): 
    resource = random.choice(resources)
    if resource == "robber":
        pairs.append((resource, 7))
        resources.remove("robber")
        continue
    number = random.choice(numbers)
    pairs.append((resource, number))
    resources.remove(resource)
    numbers.remove(number)
def draw_text(text, font, text_col, x, y):
    '''draw_text will take in a string input, font, color, and coordinates to display text'''
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))    
def hexagon(pair, coordinates):
    resource = pair[0]
    dx,dy = coordinates
    if resource == "wood":
        c = (0, 100, 0)
    if resource == "brick":
        c = (170, 100, 0)
    if resource == "ore":
        c = (128, 128, 128)
    if resource == "sheep":
        c = (0, 255, 0)
    if resource == "hay":
        c = (255, 255, 0)
    if resource == "robber":
        c = (150, 150, 0)    
    pygame.draw.polygon(screen, c, [(2*tile+dx,0+dy), (4*tile+dx,tile+dy), (4*tile+dx,3*tile+dy), (2*tile+dx,4*tile+dy), (0+dx,3*tile+dy), (0+dx,tile+dy)])
    if resource != 'robber':
        pygame.draw.circle(screen, (255, 220, 0), (2*tile+dx,2*tile+dy), tile/1.5)
        if pair[1] == 6 or pair[1] == 8:
            draw_text(str(pair[1]), num_font, (255,0,0), 1.5*tile+dx, 1.5*tile+dy)
        else:
            draw_text(str(pair[1]), num_font, (0,0,0), 1.5*tile+dx, 1.5*tile+dy)
while run:
    screen.fill((0,150,255))
    for i in pairs:
        hexagon(i, differences[di])
        if di < 18:
            di+=1
        else:
            di = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()