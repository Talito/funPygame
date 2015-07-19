import pygame
import time
import random

# global variables
WIDTH = 800
HEIGHT = 600

pygame.init()

WHITE = (255, 255, 255) #RGB
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)

# returns a "surface" for the game
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Fun Game')


STEP = 10
BLOCK_SIZE = 10
FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def snake(lead_x, lead_y, BLOCK_SIZE):
	pygame.draw.rect(gameDisplay, RED, [lead_x, lead_y, BLOCK_SIZE, BLOCK_SIZE])

def message_to_screen(msg, color): 
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [WIDTH/2, HEIGHT/2])

def gameLoop():
	gameExit = False
	gameOver = False

	lead_x = WIDTH/2
	lead_y = HEIGHT/2

	lead_x_change = 0
	lead_y_change = 0

	randAppleX = round((random.randrange(0, WIDTH-STEP))/10.0)*10
	randAppleY = round((random.randrange(0, HEIGHT-STEP))/10.0)*10

	while not gameExit:
	
		while gameOver == True:
			gameDisplay.fill(BLACK)
			message_to_screen("Game Over. Press C to play again, Q to quit", WHITE)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						gameLoop()
			
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -STEP
				elif event.key == pygame.K_RIGHT:
					lead_x_change = STEP
				elif event.key == pygame.K_UP:
					lead_y_change = -STEP
				elif event.key == pygame.K_DOWN:
					lead_y_change = STEP

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					lead_y_change = 0
		
		#BOUNDERIES
		if lead_x >= WIDTH or lead_x <= 0 or lead_y >= HEIGHT or lead_y <= 0:
			gameOver = True
		
		lead_x += lead_x_change
		lead_y += lead_y_change
		
		gameDisplay.fill(WHITE)
		pygame.draw.rect(gameDisplay, BLACK, [randAppleX, randAppleY, STEP, STEP])
		snake(lead_x, lead_y, BLOCK_SIZE)
		#gameDisplay.fill(BLACK, rect=[200, 200, 10, 10])
		
		if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX = round((random.randrange(0, WIDTH-STEP))/10.0)*10
			randAppleY = round((random.randrange(0, HEIGHT-STEP))/10.0)*10
		
		pygame.display.update()
		clock.tick(FPS)
		
	message_to_screen('You are dead', BLACK)
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	quit()
	
gameLoop()