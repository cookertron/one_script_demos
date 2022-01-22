import time
import pygame
from pygame import Rect

GRAVITY = 0.1

PLAYER_RADIUS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
PDR = Rect(0, 0, 1280, 800)
PDS = pygame.display.set_mode(PDR.size, pygame.FULLSCREEN | pygame.SCALED)

class platform:
    def __init__(s, position, width):
        s.rect = Rect(position, (width, 20))
    
    def draw(s):
        global PDS, WHITE

        pygame.draw.rect(PDS, WHITE, s.rect)

class player:
    def __init__(s, position):
        s.pos = position
        s.velocity = 0

    def draw(s):
        global PDS, PLAYER_RADIUS

        pygame.draw.circle(PDS, WHITE, s.pos, PLAYER_RADIUS)

    def update(s):
        global PLATFORMS, GRAVITY, PLAYER_RADIUS, DELTA_TIME

        s.previous_pos = (s.pos[0], s.pos[1])
        s.pos[1] += s.velocity * DELTA_TIME
        s.velocity += GRAVITY * DELTA_TIME

        if s.velocity >= 0:
            for p in PLATFORMS:
                if s.pos[0] >= p.rect.left and s.pos[0] <= p.rect.right:
                    if s.previous_pos[1] + PLAYER_RADIUS <= p.rect.top and s.pos[1] + PLAYER_RADIUS > p.rect.top:
                        s.pos = [s.pos[0], p.rect.top - PLAYER_RADIUS]
                        s.velocity = 0

        k = pygame.key.get_pressed()
        if k[pygame.K_SPACE] and s.velocity == 0:
            s.velocity = -7
        if k[pygame.K_LEFT]:
            s.pos[0] -= 3 * DELTA_TIME
        if k[pygame.K_RIGHT]:
            s.pos[0] += 3 * DELTA_TIME


PLATFORMS = [platform((0, PDR.h - 20), PDR.w),
    platform((PDR.centerx - 75, PDR.bottom - 200), 150),
    platform((PDR.centerx - 75, PDR.bottom - 400), 150),
    ]
MARIO = player([PDR.centerx, PLAYER_RADIUS])


DELTA_TIMESTAMP = time.time()

exit_demo = False
while not exit_demo:
    NOW = time.time()
    DELTA_TIME = (NOW - DELTA_TIMESTAMP) * 120
    DELTA_TIMESTAMP = NOW

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit_demo = True

    PDS.fill(BLACK)

    for p in PLATFORMS:
        p.draw()
    MARIO.draw()
    MARIO.update()

    pygame.display.update()
    #pygame.time.Clock().tick(120)

pygame.quit()
