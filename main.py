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
KHAKI = (240, 230, 140)

# returns a "surface" for the game
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Fun Game')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

STEP = 20
APPLE_THICKNESS = 30
BLOCK_SIZE = 20
FPS = 30
# the img is declared out of any logic to avoid many IOs
head = pygame.image.load('snakehead.png')
apple = pygame.image.load('apple.png')

clock = pygame.time.Clock()

smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 75)

def randAppleGen():
	randAppleX = round(random.randrange(0, WIDTH-APPLE_THICKNESS))#/10.0)*10
	randAppleY = round(random.randrange(0, HEIGHT-APPLE_THICKNESS))#/10.0)*10

	return randAppleX, randAppleY
	

def game_intro():
	intro = True
	while intro:
		gameDisplay.fill(WHITE)
		message_to_screen("WelCome to FunGame",
						GREEN,
						0,
						"large")
		message_to_screen("Eat apples and fun will come. Period.",
						RED,
						60,
						"medium")
		message_to_screen("Press S to start the game. Q to quit.",
						RED,
						90)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					gameLoop()
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.type == pygame.QUIT:
					pygame.quit()
					quit()

		pygame.display.update()
		clock.tick(15)


def snake(snakeList, BLOCK_SIZE):
	gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
	for piece in snakeList[:-1]:
		pygame.draw.rect(gameDisplay, GREEN, [piece[0], piece[1], BLOCK_SIZE, BLOCK_SIZE])

def text_objects(text, color, size="small"):
	if size == "small":
		textSurface = smallFont.render(text, True, color)
	elif size == "medium":
		textSurface = medFont.render(text, True, color)
	elif size == "large":
		textSurface = largeFont.render(text, True, color)
	return textSurface, textSurface.get_rect()
		
def message_to_screen(msg, color, y_displace=0, size="small"): # displacement from the center 
	textSurface, textRect = text_objects(msg, color, size)
	textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
	gameDisplay.blit(textSurface, textRect)

def gameLoop():
	gameExit = False
	gameOver = False

	POINTS = 0

	snakeList = [] # a Snake is made of a list of pieces
	snakeLength = 1
	
	randAppleX, randAppleY = randAppleGen()

	#Snake starting pos.
	lead_x = WIDTH/2
	lead_y = HEIGHT/2

	lead_x_change = 0
	lead_y_change = 0

	while not gameExit:
		
		
		while gameOver == True:
			gameDisplay.fill(BLACK)
			message_to_screen("Game Over", RED, -50, "large")
			message_to_screen("Press C to play again, Q to quit", WHITE, 0, "medium")
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_c:
						POINTS = 0
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

		gameDisplay.blit(apple, randApple())
		#pygame.draw.rect(gameDisplay, RED, [randAppleX, randAppleY, STEP, STEP])
		
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

		if (lead_x > randAppleX and lead_x < randAppleX + APPLE_THICKNESS) or ((lead_x + BLOCK_SIZE) > randAppleX and (lead_x + BLOCK_SIZE) < (randAppleX + APPLE_THICKNESS)):
			if (lead_y > randAppleY and lead_y < randAppleY + APPLE_THICKNESS) or ((lead_y + BLOCK_SIZE) > randAppleY and (lead_y + BLOCK_SIZE) < (randAppleY + APPLE_THICKNESS)):	
				randAppleX, randAppleY = randAppleGen()
				snakeLength += 1
				POINTS += (1+(snakeLength/3))

		message_to_screen(str(POINTS), KHAKI, -200, "large")
		# alternative:
		# text = smallfont.render(str(POINTS), True black)
		# gameDisplay.blit(text, [0, 0])
		
		pygame.display.update()
		clock.tick(FPS)
	
	gameDisplay.fill(BLACK)
	message_to_screen('FUNGAME 2015 :)', WHITE, 0)
	pygame.display.update()
	time.sleep(1)
	pygame.quit()
	quit()

game_intro()	