import pygame
import os
from Reversi import Reversi
import sys

class Reversi_GUI:
	def __init__(self):

		pygame.init()
		pygame.display.init()
		self.screen_width = 700
		self.screen_height = 560
		self.screen = pygame.display.set_mode([self.screen_width,self.screen_height])

 		pygame.display.set_caption('Play Reversi')
 		self.boardColor = (38, 102, 28)
 		self.lineColor = (183,168,168)

 		self.playerTileColor = (255,255,255)
 		self.computerTileColor = (0,0,0)
 		self.tileRadius = 21
 		
 		self.textFont = pygame.font.SysFont("Times", 15)
 		self.fontColor = (255,204,153)

 		self.user_pos = "None"
 		self.computer_pos = "None"


 		#self.font = pygame.font.SysFont(fontStyle, fontSize)
 		self.boardX = 250
 		self.boardY = 60
 		self.boardSize = 400

 		self.user_Tile = "X"
 		self.computer_Tile = "0"

 		#self.loadImages()
 

 	# function that loads all necessary images from directory GUI.
	def loadImages(self):

		self.player_Tile = pygame.image.load(os.path.join("images","Reversi_Player_Tile.png")).convert()
		#self.player_Tile = pygame.transform.scale(self.white_queen, (self.square_size,self.square_size))

		self.computer_Tile = pygame.image.load(os.path.join("images","Reversi_Computer_Tile.png")).convert()
		#self.computer_Tile = pygame.transform.scale(self.white_king, (self.square_size,self.square_size))



	def updatePos(self,role,x,y):
		if role == 1:
			self.user_pos = (x,y)
		else:
			self.computer_pos = (x,y)
		return 


	# function that draws the reversi board, which is a 8*8 chessboard.
	def drawBoard(self,board):
		self.screen.fill((74,42,29))
		pygame.draw.rect(self.screen, self.boardColor,pygame.Rect(self.boardX ,self.boardY, self.boardSize, self.boardSize))
		
		# draw all horizontal lines for the board.
		for i in range(9):
			start_pos = (self.boardX, self.boardY + i*50)
			end_pos = (self.boardX + self.boardSize,self.boardY + i*50)
			pygame.draw.line(self.screen, self.lineColor,start_pos, end_pos, 1)

		# # draw all vertical lines for the board. 
		for i in range(9):
			start_pos = (self.boardX + i*50, self.boardY)
			end_pos = (self.boardX + i*50, self.boardY + self.boardSize)
			pygame.draw.line(self.screen, self.lineColor,start_pos, end_pos, 1)

		# draw all tiles on the board. 
		for i in range(8):
			for j in range(8):
				posY_ = self.boardY + 50 * i + 25
				posX_ = self.boardX + 50 * j + 25
				pos_ = (posX_, posY_)

				if board[i][j] == "X":
					pygame.draw.circle(self.screen, self.playerTileColor, pos_, self.tileRadius, 0)
				elif board[i][j] == "0":
					pygame.draw.circle(self.screen, self.computerTileColor, pos_, self.tileRadius, 0)
		
		self.update_Text()



	# function that writes text to the screen 	
	def writeText(self,computerScore, playerScore, computerMove, playerMove):
		return

	def reverseTiles(self,oldBoard,newBoard):
		return
	
	# This function checks if user clicks area within the board. 
	# also checks if user's choice at least flips one opponent's tile on the board. 
	def checkValid(self,x,y,board,tile,oppositetile):
		valid = True
		if 250 > x or x > 650:
			valid = False
		if 60 > y or y > 460:
			valid = False
		(x,y) =  self.convertCoordinate(1,(x,y))
		hasTile = False
		for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
			go_x = x
			go_y = y
			go_x  += xdirection
			go_y += ydirection
			while self.onboard(go_x,go_y) and board[go_y][go_x] == oppositetile:
				print(go_x,go_y)
				go_x += xdirection
				go_y += ydirection
			if self.onboard(go_x,go_y) and board[go_y][go_x] == tile:
				
				hasTile = True
		
		return (valid and hasTile)

	def onboard(self,x, y):
		return x >= 0 and x <= 7 and y >= 0 and y <=7

	# This converts the screen coordinate to array coordiante when parameter is 1, and backwards when parameter is 0. ONLY VALID MOVE.
	def convertCoordinate(self,parameter, (x,y)):
		pos = (0,0)
		if parameter == 1:
			x_ = (x - self.boardX) / 50
			y_ = (y - self.boardY) / 50
			pos = (x_, y_)

		elif parameter == 0:

			posX = self.boardX + 50 * x_ + self.tileRadius
			posY = self.boardY + 50 * y_ + self.tileRadius
			pos = (posX, posY)

		return pos

	def update_Text(self,):
		# updating the scores of both user and computer. 
		user_score, computer_score = reversi.getscore(self.user_Tile, self.computer_Tile)
		print user_score
		user_score_string = "User Score: " + str(user_score)
		computer_score_string = "Computer score: " + str(computer_score)
		user_score = self.textFont.render(user_score_string,True,self.fontColor)
		computer_score = self.textFont.render(computer_score_string,True,self.fontColor)
		self.screen.blit(user_score,(35,150))
		self.screen.blit(computer_score,(35,300))

		# updating the position of a new tile placed by the user and and the computer. 

		user_pos_string = "New Tile Position: " + str(self.user_pos)
		computer_pos_string = "New Tile position: " + str(self.computer_pos)

		user_pos_string = self.textFont.render(user_pos_string,True,self.fontColor)
		computer_pos_string = self.textFont.render(computer_pos_string,True,self.fontColor)
		self.screen.blit(user_pos_string,(35,200))
		self.screen.blit(computer_pos_string,(35,350))

		return


	# functino that draws tiles on the chess board according to the updated board, board is a two-dimensional array with its entries specifying tiles placed on the board. 
	# (x,y) is the screen coordinate. 
	def placeTile(self,(x,y)):
		return

	def run_game(self,board,reversi):
		# board = initializeBoard() (*init* from main.py)
		self.drawBoard(board)

		
		reverse = False
		waitForComputer = False
		state = 0
		(p_x,p_y) = (1,0)
		while 1:
			for event in pygame.event.get():
				
				if event.type is pygame.QUIT:
					sys.exit()
				elif event.type is pygame.MOUSEBUTTONDOWN:
					(mouseX,mouseY) = pygame.mouse.get_pos()
					print (mouseX,mouseY)
					# call functions from main that returns an updated board with new tiles being placed. 
					if self.checkValid(mouseX,mouseY,board,"X","0"):
						(p_x,p_y) = self.convertCoordinate(1,(mouseX,mouseY))
						print("ready to update")
						self.updatePos(1,p_x+1,p_y+1)
						board = reversi.updateboard(p_x,p_y,self.user_Tile)
						reverse = True
						waitForComputer = True
						state = 1
						
				else:
					if reverse is True:
						print "reverse"
						#flip all tiles necessary	
						if state == 1:
							board = reversi.reverse(p_x,p_y,self.user_Tile,self.computer_Tile)
						elif state == 2:
							board = reversi.reverse(p_x,p_y,self.computer_Tile,self.user_Tile)
						
						reverse = False
						state = 0

				 	elif waitForComputer is True:

				 		bestMove = reversi.searchbestmoves(self.computer_Tile, self.user_Tile)
				 		if bestMove != None:
				 			board = reversi.updateboard(p_x,p_y,self.computer_Tile)
							self.updatePos(0,p_x+1,p_y+1)
							print "waitForComputer"
				 			reverse = True
				 			state = 2
				 		waitForComputer  = False
				 		


				# update board
				self.drawBoard(board)

			# allow any update of the display to be visible
			pygame.display.flip()
			pygame.time.wait(120)
  

# we need a updateBoard function that gives the newly updated two dimensional array. Also need the updated computer and player score. 
if __name__ == "__main__":
	# create the 8 * 8 grid.(variable:board)
    reversi = Reversi()
        # aske the user to input the tile he chooses to play and also assign computer the other tile. 
    computertile = reversi.assigntile('X')
       # print the initial board with four tiles in the center.
    reversi.initiateboard()
    board = reversi.getBoard()
    game = Reversi_GUI()
    game.run_game(board,reversi)

