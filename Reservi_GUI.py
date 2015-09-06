import pygame
import os


class Reversi_GUI:
	def _init_(self):

		pygame.init()
		self.screen_width = 600
		self.screen_height = 600
 		self.screen = pygame.display.set_mode([screen_width,screen_height])
 		pygame.display.set_caption('Play Reversi')

 		self.boardColor = (137, 42, 96)
 		self.lineColor = (183,168,168)
 		self.playerTileColor = (255,255,255)
 		self.computerTileColor = (0,0,0)
 		self.tileRadius = 70

 		self.fontStyle = ""
 		self.fontSize = 30
 		self.font = pygame.font.SysFont(fontStyle, fontSize)

 		self.boardX = 150
 		self.boardY = 100
 		self.boardSize = 400

 		self.loadImages()

 	# function that loads all necessary images from directory GUI.
	def loadImages():

		self.player_Tile = pygame.image.load(os.path.join("images","Reversi_Player_Tile.png")).convert()
		#self.player_Tile = pygame.transform.scale(self.white_queen, (self.square_size,self.square_size))

		self.computer_Tile = pygame.image.load(os.path.join("images","Reversi_Computer_Tile.png")).convert()
		#self.computer_Tile = pygame.transform.scale(self.white_king, (self.square_size,self.square_size))


	# function that draws the reversi board, which is a 8*8 chessboard.
	def drawBoard(board):
		pygame.draw.rect(screen, self.boardColor,pygame.Rect(self.boardX ,self.boardY, self.boardSize, self.boardSize))
		
		# draw all horizontal lines for the board.
		for i in range(9):
			start_pos = (self.boardX, self.boardY + i*50)
			end_pos = (self.boardX + self.boardSize,self.boardY + i*50)
			pygame.draw.line(screen, self.lineColor,start_pos, end_pos, width=1)

		# draw all vertical lines for the board. 
		for i in range(9):
			start_pos = (self.boardX + i*50, self.boardY)
			end_pos = (self.boardX + i*50, self.boardY + self.boardSize)
			pygame.draw.line(screen, self.lineColor,start_pos, end_pos, width=1)

		# draw all tiles on the board. 
		for i in range(8):
			for j in range(8):
				posX = self.boardX + 50 * i + 25
				posY = self.boardY + 50 * j + 25
				pos = (posX, posY)

				if board[i][j] = "X":
					pygame.draw.circle(screen, self.playerTileColor, pos, self.tileRadius, width=0)
				elif board[i][j] = "0":
					pygame.draw.circle(screen, self.computerTileColor, pos, self.tileRadius, width=0)


	# function that writes text to the screen 	
	def writeText(computerScore, playerScore, computerMove, playerMove):

	
	def reverseTiles(oldBoard,newBoard):

	
	
	# This function checks if user clicks area within the board. 
	def checkValid(x,y):
		valid = True
		if x < 150 or x > 550:
			valid = False
		if y < 100 or y > 500:
			valid = False
		return valid

	# This converts the screen coordinate to array coordiante when parameter is 1, and backwards when parameter is 0. ONLY VALID MOVE.
	def convertCoordinate(parameter, (x,y)):
		pos = (0,0)
		if parameter == '1':
			x_ = (x - self.boardX) / 50
			y_ = (y - self.boardY) / 50
			pos = (x_, y_)

		elif parameter == '0':

			posX = self.boardX + 50 * x_ + 25
			posY = self.boardY + 50 * y_ + 25
			pos = (posX, posY)



	# functino that draws tiles on the chess board according to the updated board, board is a two-dimensional array with its entries specifying tiles placed on the board. 
	# (x,y) is the screen coordinate. 
	def placeTile((x,y)):
		


	def run_game():
		# board = initializeBoard() (*init* from main.py)
		drawBoard()

		while 1:
			for event in pygame.event.get():
				if event.type is pygame.QUIT:
					sys.exit()
				elif event.type is KEYDOWN:
					(mouseX,mouseY) = pygame.mouse.get_pos()
					# call functions from main that returns an updated board with new tiles being placed. 
					# newBoard = updateBoard(...)

					#placing player's tile on the board
					placeTile(newBoard)

					#flip all tiles necessary
					reverseTiles(board,newBoard)

					#writeText(computerScore, playerScore, computerMove, playerMove)

					# watch out for pointer issue here. 
					board = newBoard

					#get computer's tile, return newBoard with computer's tiles placed on it. 

					drawTiles(newBoard)

					#flip all tiles necessary
					reverseTiles(board,newBoard)

					board = newBoard

				else:
					drawTiles(board)



# we need a updateBoard function that gives the newly updated two dimensional array. Also need the updated computer and player score. 














