import pygame
import os
from Reversi import Reversi
import sys
from Reversi_AI import Reversi_AI

class Reversi_GUI:
	def __init__(self):

		pygame.init()
		pygame.display.init()
		self.screen_width = 700
		self.screen_height = 460
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
		self.boardY = 30
		self.boardSize = 400
		self.user_Tile = "X"
		self.computer_Tile = "0"

		#information board
		self.infoBoardColor = (94,61,47)
		self.infoBoardx = 30
		self.infoBoardy = 30
		self.infoBoardwidth = 195
		self.infoBoardheight = 150


		self.loadImages()

 	# function that loads all necessary images from directory GUI.
	def loadImages(self):

		self.player_Tile_image = pygame.image.load("white_tile.bmp").convert()
		self.player_Tile_image = pygame.transform.scale(self.player_Tile_image, (49,49))

		self.computer_Tile_image = pygame.image.load("black_tile.bmp").convert()
		self.computer_Tile_image = pygame.transform.scale(self.computer_Tile_image, (49,49))

	def updatePos(self,role,x,y):
		if role == 1:
			self.user_pos = (x,y)
		else:
			self.computer_pos = (x,y)
		return 

	# function that draws the reversi board, which is a 8*8 chessboard.
	def drawBoard(self,board,yield_):
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
				posY_ = self.boardY + 50 * i +1
				posX_ = self.boardX + 50 * j +1
				pos_ = (posX_, posY_)

				if board[i][j] == "X":
					#pygame.draw.circle(self.screen, self.playerTileColor, pos_, self.tileRadius, 0)
					self.screen.blit(self.player_Tile_image, pos_)
				elif board[i][j] == "0":
					#pygame.draw.circle(self.screen, self.computerTileColor, pos_, self.tileRadius, 0)
					self.screen.blit(self.computer_Tile_image, pos_)
		
		self.update_Text(yield_)

	# function that writes text to the screen 	
	def endOfGame(self,computerScore, playerScore):
		end = False
		if computerScore + playerScore == 64:
			end = True
		elif computerScore == 0 or playerScore == 0:
			end = True
		return end

	# This function checks if user clicks area within the board. 
	# also checks if user's choice at least flips one opponent's tile on the board. 
	def checkValid(self,x,y,board,tile,oppositetile):
		valid = True
		if self.boardX > x or x > self.boardSize + self.boardX:
			valid = False
		if self.boardY > y or y > self.boardSize + self.boardY:
			valid = False
		(x,y) =  self.convertCoordinate(1,(x,y))
		hasTile = False
		for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
			hasOpp = False
			go_x = x
			go_y = y
			go_x  += xdirection
			go_y += ydirection
			while self.onboard(go_x,go_y) and board[go_y][go_x] == oppositetile:	
				go_x += xdirection
				go_y += ydirection
				hasOpp = True
			if hasOpp and self.onboard(go_x,go_y) and board[go_y][go_x] == tile :		
				hasTile = True
		return (valid and hasTile)

	def onboard(self,x, y):
		return x >= 0 and x <= 7 and y >= 0 and y <=7

	# This converts the screen coordinate to array coordiante when parameter is 1, and backwards when parameter is 0. ONLY VALID MOVE.
	def convertCoordinate(self,parameter, tuplein):
		pos = (0,0)
		x = tuplein[0]
		y = tuplein[1]
		if parameter == 1:
			x_ = (x - self.boardX) / 50
			y_ = (y - self.boardY) / 50
			pos = (x_, y_)

		elif parameter == 0:

			posX = self.boardX + 50 * x_ + self.tileRadius
			posY = self.boardY + 50 * y_ + self.tileRadius
			pos = (posX, posY)

		return pos

		# when yield is 0, there is no yield. When yield is 1, yield to user .When yield is 2, yield to computer
	# call the restart function inside the update_text function.
	def update_Text(self,yield_):

		# user's score board
		pygame.draw.rect(self.screen, self.infoBoardColor,pygame.Rect(self.infoBoardx ,self.infoBoardy, self.infoBoardwidth, self.infoBoardheight))

		# computer's score board

		pygame.draw.rect(self.screen, self.infoBoardColor,pygame.Rect(self.infoBoardx ,self.infoBoardy + self.infoBoardheight + 20, self.infoBoardwidth,self.infoBoardheight))

		# draw user tile on the info board. 
		self.screen.blit(self.player_Tile_image,(self.infoBoardx + 10,self.infoBoardy + 10))
		# draw computer tile on the info board.
		self.screen.blit(self.computer_Tile_image,(self.infoBoardx + 10,self.infoBoardy + self.infoBoardheight + 20 + 10 ))

		# write down "You" and "computer".

		user_string = "You"
		computer_string = "Computer" 

		user_string = self.textFont.render(user_string,True,self.fontColor)
		computer_string = self.textFont.render(computer_string,True,self.fontColor)
		self.screen.blit(user_string,(self.infoBoardx + 70,self.infoBoardy + 30))
		self.screen.blit(computer_string,(self.infoBoardx + 70,self.infoBoardy + self.infoBoardheight + 20 + 30))


		# updating the scores of both user and computer. 
		user_score, computer_score = reversi.getscore(self.user_Tile, self.computer_Tile)
		# checking that if the game has already ended
		end = False
		end = self.endOfGame(computer_score, user_score)
		
		user_score_string = "User Score: " + str(user_score)
		computer_score_string = "Computer score: " + str(computer_score)

		user_score = self.textFont.render(user_score_string,True,self.fontColor)
		computer_score = self.textFont.render(computer_score_string,True,self.fontColor)
		self.screen.blit(user_score,(self.infoBoardx + 10,self.infoBoardy + 80))
		self.screen.blit(computer_score,(self.infoBoardx + 10,self.infoBoardy + self.infoBoardheight + 20 + 10 + 70))

		# updating the position of a new tile placed by the user and and the computer. 

		user_pos_string = "Current Position: " + str(self.user_pos)
		computer_pos_string = "Current position: " + str(self.computer_pos)

		user_pos_string = self.textFont.render(user_pos_string,True,self.fontColor)
		computer_pos_string = self.textFont.render(computer_pos_string,True,self.fontColor)
		self.screen.blit(user_pos_string,(self.infoBoardx + 10,self.infoBoardy + 120))
		self.screen.blit(computer_pos_string,(self.infoBoardx + 10,self.infoBoardy + self.infoBoardheight + 20 + 10 + 50 + 60))

		endString = " "
		if end == True:
			print("computer_score",computer_score)
			print("user_score",user_score)
			if computer_score > user_score:
				endString = "The computer wins!"
			elif computer_score < user_score:
				endString = "The user wins!"
			elif computer_scoren == user_score:
				endString = "Both win!"
			restartString = "Press R to restart."
			end_string = self.textFont.render(endString,True,self.fontColor)
			restart_string = self.textFont.render(restartString,True,self.fontColor)
			self.screen.blit(end_string,(35,400))
			self.screen.blit(restart_string,(25,440))

		else:
			yString = " "
			if yield_ == 1:
				yString = "Yield to User"
			elif yield_ == 2:
				yString = "Yield to Computer"
			yield_string = self.textFont.render(yString,True,self.fontColor)
			self.screen.blit(yield_string,(35,400))

		return end

	def run_game(self,reversi):
		end = False
		board = reversi.getBoard()
		AI = Reversi_AI()
		end = self.drawBoard(board,0)
		yield_ = 0
		waitForComputer = False
		waitForUser = True

		while 1:
			for event in pygame.event.get():
				if end == True:
					board = reversi.getBoard()
					end = self.drawBoard(board,0)			
				elif event.type is pygame.QUIT:
					sys.exit()	
				elif event.type is pygame.MOUSEBUTTONDOWN:
					(mouseX,mouseY) = pygame.mouse.get_pos()
					if waitForUser is True:
						if len(AI.searchAllmoves(board,"X","0")) > 0:	
							yield_ = 0		
							if self.checkValid(mouseX,mouseY,board,"X","0"):
								(user_x,user_y) = self.convertCoordinate(1,(mouseX,mouseY))
								self.updatePos(1,user_x+1,user_y+1)
								board = reversi.updateboard(user_x,user_y,self.user_Tile)
								end = self.drawBoard(board,yield_)
								pygame.display.flip()
								pygame.time.wait(200)
								# reverse tiles
								board = reversi.reverse(user_x,user_y,self.user_Tile,self.computer_Tile)
								end = self.drawBoard(board,yield_)
								# allow any update of the display to be visible
								pygame.display.flip()
								pygame.time.wait(200)
								waitForComputer = True
								waitForUser = False
							else:
								print("invalid move")
						else:
							print("yield to computer")
							yield_ = 2
							waitForComputer = True
							waitForUser = False
							

				elif waitForComputer is True:
					bestMove = reversi.searchbestmoves(self.computer_Tile, self.user_Tile)
					if bestMove != None:
							yield_ = 0
							com_x = bestMove[0]
							com_y = bestMove[1]
							board = reversi.updateboard(com_x,com_y,self.computer_Tile)
							self.updatePos(0,com_x+1,com_y+1)
							end = self.drawBoard(board,yield_)
							pygame.display.flip()
							pygame.time.wait(200)
							print("waitForComputer")
						# reverse tiles
							board = reversi.reverse(com_x,com_y,self.computer_Tile,self.user_Tile)			 		
					else: 
						print("yield to user")
						yield_ = 1	
				 		
					waitForComputer  = False
					waitForUser = True
				 	
				 	# when waitForUser is True but user did not click on the board.
				else:
					if len(AI.searchAllmoves(board,"X","0")) == 0:
						waitForComputer = True
						waitForUser = False
						yield_ = 2
						print("yield to computer")
						


				# update board

				end = self.drawBoard(board,yield_)
			# allow any update of the display to be visible
			pygame.display.flip()
			if yield_ != 0:
				pygame.time.wait(1000)
			else: 
				pygame.time.wait(200)
  

# we need a updateBoard function that gives the newly updated two dimensional array. Also need the updated computer and player score. 
if __name__ == "__main__":
	# create the 8 * 8 grid.(variable:board)
    reversi = Reversi()
        # aske the user to input the tile he chooses to play and also assign computer the other tile. 
    computertile = reversi.assigntile('X')
       # print the initial board with four tiles in the center.
    reversi.initiateboard()
    game = Reversi_GUI()
    game.run_game(reversi)

