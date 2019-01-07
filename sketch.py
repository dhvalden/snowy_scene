import sys
import pygame
import snowflake
from snowflake import Snowflake

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAVITY = 0.01

path = 'snowy_scene/'

screen = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

surface = pygame.display.set_mode(screen)
pygame.display.set_caption('Snowy Scene')
clock = pygame.time.Clock()

sheet = pygame.image.load('flakes32.png').convert()
sheet.set_colorkey((0, 0, 0))

images = []

for x in range(0, sheet.get_width(), 32):
    for y in range(0, sheet.get_height(), 32):
        image = pygame.Surface((32, 32))
        image.blit(sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        images.append(image)    

snowflake.init(DISPLAY_WIDTH, DISPLAY_HEIGHT, surface, images)

snow = []
numberFlakes = 300

def createSnow(num):
    for i in range(0, num):
        snow.append(Snowflake())

def main():
    """Main animation loop"""
    stop = False

    createSnow(numberFlakes)

    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

        surface.fill(BLACK)

        for flake in snow:
            flake.applyForce(0, GRAVITY)
            flake.update()
            flake.draw()

        pygame.display.update()

        clock.tick(60)

main()
pygame.quit()
sys.exit()
