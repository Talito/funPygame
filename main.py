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
# the img is declared is out any logic to avoid many IOs
head = pygame.image.load('C:/Users/Josetalito/Desktop/CS/Pygame/snakehead.png')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def snake(snakeList, BLOCK_SIZE):

	gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

	for piece in snakeList[:-1]:
		pygame.draw.rect(gameDisplay, RED, [piece[0], piece[1], BLOCK_SIZE, BLOCK_SIZE])

def text_objects(text, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()
		
def message_to_screen(msg, color): 
	textSurface, textRect = text_objects(msg, color)
	#screen_text = font.render(msg, True, color)
	#gameDisplay.blit(screen_text, [WIDTH/2, HEIGHT/2])
	textRect.center = (WIDTH/2), (HEIGHT/2)
	gameDisplay.fill(BLACK)
	gameDisplay.blit(textSurface, textRect)


def gameLoop():
	gameExit = False
	gameOver = False

	snakeList = [] # a Snake is made of a list of pieces
	snakeLength = 1

	#Snake starting pos.
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
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -STEP
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = STEP
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -STEP
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = STEP
					lead_x_change = 0

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
		
		# the magic, growing the snake
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		for eachPiece in snakeList[:-1]:
			if eachPiece == snakeHead:
				gameOver = True
		
		snake(snakeList, BLOCK_SIZE)
		
		if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX = round((random.randrange(0, WIDTH-STEP))/10.0)*10
			randAppleY = round((random.randrange(0, HEIGHT-STEP))/10.0)*10
			snakeLength += 1
		
		pygame.display.update()
		clock.tick(FPS)
		
	message_to_screen('You are dead', WHITE)
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	quit()
	
gameLoop()