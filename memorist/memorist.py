import pygame, sys, random
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((1060, 560))
BLUE=(0, 0, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

NUMBER_OF_COLS = 5
NUMBER_OF_ROWS = 4

VALUES = []

for ROWS in range(0, NUMBER_OF_ROWS):
    SUBVALUES = []
    for COLS in range(0, NUMBER_OF_COLS):
        SUBVALUES.append(random.randint(100, 999))
    VALUES.append(SUBVALUES)

print(VALUES)

font = pygame.font.Font(None, 32)
TEXT=[]

for ROWS in range(0, NUMBER_OF_ROWS):
    SUBTEXT = []
    for COLS in range(0, NUMBER_OF_COLS):
        SUBTEXT.append(font.render(str(VALUES[ROWS][COLS]), True, BLUE))
    TEXT.append(SUBTEXT)
print(TEXT)

pygame.display.set_caption('Memorist')
while True: # main game loop
    for event in pygame.event.get():

        SCREEN.fill((255, 255, 255))
        DONE = False 
        for ROWS in range(0, NUMBER_OF_ROWS):
            for COLS in range(0, NUMBER_OF_COLS):
                SCREEN.blit(TEXT[ROWS][COLS], (100+(COLS*200), 70+(ROWS*120)))

        pygame.display.flip()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            SCREEN.fill((255, 255, 255))
            pygame.display.flip()
            while not DONE:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        DONE = True
    
    pygame.display.update()
