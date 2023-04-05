from pygame.locals import *
from random import randint
import os
import pygame, sys
pygame.init()
 
# init font
pygame.font.init()
my_font = pygame.font.Font('./CroissantOne-Regular.ttf', 18)

# vocab
input_vocab = []
output_vocab = []
with open("./vocab.txt", "r") as f:
  for line in f: 
    x = line.split("\t") 
    input_vocab.append(x[0])
    output_vocab.append(x[1][:-1]) 

# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
    
# asteriods
numAsteroids = 3
locations = [0 for _ in range(numAsteroids)]
textIndx = [0 for _ in range(numAsteroids)]
speeds = [0 for _ in range(numAsteroids)]
enabled = [True for _ in range(numAsteroids)]
def resetAsteroids ():
  locations[0] = (randint(60, 70), randint(10, 100))
  locations[1] = (randint(180, 250), randint(10, 100))
  locations[2] = (randint(350, 370), randint(10, 100))
  for i in range(numAsteroids):
    textIndx[i] = randint(0, len(input_vocab)-1) 
    speeds[i] = randint(1, 5) / 10
    enabled[i] = True
resetAsteroids()

def checkAsteroid (str):
  for i in range(numAsteroids):
    if str.lower() == output_vocab[textIndx[i]].lower():
      enabled[i] = False
     
  
# load images
background = pygame.image.load( "C:\\Users\\eshaa\\OneDrive\\Desktop\\Coding\\FrenchGame\\sprites\\Background.png").convert()

asteroid = pygame.image.load( "C:\\Users\\eshaa\\OneDrive\\Desktop\\Coding\\FrenchGame\\sprites\\Rock.png")
asteroid = pygame.transform.scale(asteroid, (100, 100))
asteroid = asteroid.convert()
 
# text functions
textInput = ""

# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      global textInput, checkAsteroid
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        name = pygame.key.name(event.key)
        if name == "backspace": 
          textInput = textInput[:-1]
        elif name == "space":
          textInput += " "
        elif name == "return":
          checkAsteroid(textInput)
          textInput = ""
        else:
          textInput += name 

    # draw background
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    
    
    # detect if all three asteroids
    if sum(enabled) == 0: resetAsteroids()
    
    # draw asteriods
    for i in range(numAsteroids): 
      if enabled[i]:
        locations[i] = (locations[i][0], locations[i][1] + speeds[i])

        screen.blit(asteroid, locations[i]) 
        
        # text
        text_surface = my_font.render(input_vocab[textIndx[i]], False, (255, 255, 255))
        screen.blit(text_surface, (locations[i][0], locations[i][1]+100))

      # detect if one asteroiud is below
      if locations[i][1] >= 600:
        print("You died!")
        exit(0)

    # draw what user put out
    text_surface = my_font.render(textInput, False, (255, 255, 255))
    screen.blit(text_surface, (200, 700))
    
    # update
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()