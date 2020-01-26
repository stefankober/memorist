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

font = pygame.font.Font(None, 32)
TEXT=[]

for ROWS in range(0, NUMBER_OF_ROWS):
    SUBTEXT = []
    for COLS in range(0, NUMBER_OF_COLS):
        SUBTEXT.append(font.render(str(VALUES[ROWS][COLS]), True, BLUE))
    TEXT.append(SUBTEXT)

def please_write_down():
    if random.randint(0,1) == 0:
        RANDOM_COL = random.randint(0, NUMBER_OF_COLS-1)
        print("column" + str(RANDOM_COL+1))
    else:
        RANDOM_ROW = random.randint(0, NUMBER_OF_ROWS-1)
        print("row" + str(RANDOM_ROW+1))

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
            please_write_down()

            while not DONE:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        DONE = True
    
    pygame.display.update()
