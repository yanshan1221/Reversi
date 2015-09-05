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
	def drawBoard():
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

	# function that writes text to the screen 	
	def writeText(computerScore, playerScore, computerMove, playerMove):

	
	def reverseTiles(oldBoard,newBoard):


	# functino that draws tiles on the chess board according to the updated board, board is a two-dimensional array with its entries specifying tiles placed on the board. 

	def drawTiles(board):


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
					drawTiles(newBoard)

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














