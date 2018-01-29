import pygame, sys
import serial
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600)) #window size
pygame.display.set_caption('Hello World!') #header of window
s = serial.Serial("/dev/ttyACM0")


while True: #main game loop
    l = s.readline()
    x = l.rstrip().split(",")
    if len(x) == 3:#make sure list has all three rgb values
        rgb = [int(val) for val in x]
    else:
        rgb = (255,255,255)
    pygame.draw.rect(DISPLAYSURF, rgb, (0,0,800,600))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
   
