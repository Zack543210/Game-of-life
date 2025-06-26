import pygame
from random import randint
from copy import deepcopy

ZOOM = 5
TILE_SIZE = 4
WIDTH, HEIGHT = 320*ZOOM, 180*ZOOM

RES = WIDTH, HEIGHT
TILE = TILE_SIZE*ZOOM
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 5

nextField = [[0 for i in range(W)] for j in range(H)]
currentField = [[randint(0, 1) for i in range(W)] for j in range(H)]

def checkCell(currentField, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if currentField[j][i]:
                count += 1

    if currentField[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

while True:
    surface.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()

    #draw grid
    #verticles
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0),
                      (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    #horizontals
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y),
                      (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    #draw life
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if currentField[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                 (x * TILE + 2,y * TILE + 2, TILE - 2, TILE - 2))
            nextField[y][x] = checkCell(currentField, x, y)

    currentField = deepcopy(nextField)

    pygame.display.flip()
    clock.tick(FPS)
