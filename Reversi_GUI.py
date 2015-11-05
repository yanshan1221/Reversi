import pygame
import os
from Reversi import Reversi
import sys
from Reversi_AI import Reversi_AI

"""
	Reversi_GUI.py runs the reversi game with a user interface using Python2.7 32bits. 
	The 8*8 game board is displayed as a 400(pixel)*400(pixel) green game board. Black tile representsthe computer 
	and white tile represents the user. On the left panel of the window is the information board thatdisplays the 
	current scores of the user and the computer. At the bottom left, hint reminds user of the current status of the
	game. When there is not a valid move on the board for either the user or the computer, it will display "yield to
	user/computer". At the end of the game, it will display "user/computer wins. Press R to restart"

	Example:
		python2.7-32 Reversi_GUI.py

"""
class Reversi_GUI:

	""" Reversi_GUI is a class that creates Reversi_GUI object containing all methods for running the game with a user interface
	"""

	def __init__(self):
		pygame.init()
		pygame.display.init()
		self.screenWidth = 700
		self.screenHeight = 460
		self.screen = pygame.display.set_mode([self.screenWidth,self.screenHeight])

		pygame.display.set_caption('Play Reversi')
		self.boardColor = (38, 102, 28)
		self.lineColor = (183,168,168)

		self.playerTileColor = (255,255,255)
		self.computerTileColor = (0,0,0)
		self.tileRadius = 21

		self.textFont = pygame.font.SysFont("Times", 15)
		self.fontColor = (255,204,153)

		self.userPos = "None"
		self.computerPos = "None"

		self.boardX = 250
		self.boardY = 30
		self.boardSize = 400
		self.userTile = "X"
		self.computerTile = "0"

		#information board
		self.infoBoardColor = (94,61,47)
		self.infoBoardx = 30
		self.infoBoardy = 30
		self.infoBoardwidth = 195
		self.infoBoardheight = 150

		self.loadImages()

	def loadImages(self):
		"""
			loadImages loads all necessary pictures in bmp format for the program
		"""

		self.playerTileImage = pygame.image.load("white_tile.bmp").convert()
		self.playerTileImage = pygame.transform.scale(self.playerTileImage, (49,49)) # load the white tile image

		self.computerTileImage = pygame.image.load("black_tile.bmp").convert()
		self.computerTileImage = pygame.transform.scale(self.computerTileImage, (49,49)) # load the black tile image

	def updatePos(self,role,x,y):
		"""
		updatePos updates the position on board where the user or the computer is about to place a new tile.

		Args:
			x(int): x coordinate of the position for a new tile
			y(int): y coordinate of the position for a new tile
			role(int): 1 if user and 0 if computer
		"""
		if role == 1:
			self.userPos = (x,y)
		else:
			self.computerPos = (x,y)
		return 


	def drawBoard(self,reversi,yield_):
		"""
		drawBoard draws the 8*8 board and displays information about scores and status of the game on the screen.

		Args:
		    board(int[][]): a 2-D array representing the board configuration
		    yield_(int): yield_ = 1 indicates that one player can not make a valid move at this round and play passes back to the other player

		Returns:
			end(boolean): true when the game ends, false otherwise
		"""

		self.screen.fill((74,42,29))
		pygame.draw.rect(self.screen, self.boardColor,pygame.Rect(self.boardX ,self.boardY, self.boardSize, self.boardSize))
		
		board = reversi.getBoard()
		for i in range(9): # draw all horizontal lines for the board.
			startPos = (self.boardX, self.boardY + i*50)
			endPos = (self.boardX + self.boardSize,self.boardY + i*50)
			pygame.draw.line(self.screen, self.lineColor,startPos, endPos, 1)

		for i in range(9): # draw all vertical lines for the board. 
			startPos = (self.boardX + i*50, self.boardY)
			endPos = (self.boardX + i*50, self.boardY + self.boardSize)
			pygame.draw.line(self.screen, self.lineColor,startPos, endPos, 1)
		
		for i in range(8): # draw all tiles on the board. 
			for j in range(8):
				posY_ = self.boardY + 50 * i +1
				posX_ = self.boardX + 50 * j +1
				pos_ = (posX_, posY_)

				if board[i][j] == "X":		
					self.screen.blit(self.playerTileImage, pos_)
				elif board[i][j] == "0":
					self.screen.blit(self.computerTileImage, pos_)

		end = self.update_Text(reversi,yield_) # write information about scores and status on the board, check if the game reaches its end.
		return end

	
	def endOfGame(self,computerScore, playerScore):
		"""
		endOfGame checks if the game has ended by looking at the number of tiles on the board.

		Args:
		    computerScore(int): current score of the computerScore
		    playerScore(int): current score of the user

		Returns:
			end(boolean): true when the game has ended, false otherwise
		"""
		end = False
		if computerScore + playerScore == 64: # the game ends when the board is filled with tiles.
			end = True
		elif computerScore == 0 or playerScore == 0: # the game ends when one player's tiles have completely dominate the board. 
			end = True
		return end

	
	def checkValid(self,x,y,board,playerTile,opponentTile):
		"""
		checkValid checks if a move is valid

		Args:
			x(int),y(int): the x and y coordinate of the move
			playerTile(str),opponentTile(str): strings representing player and his opponent
			board(int[][]): 2-D array representing board configuration

		Returns:
			True if the move is valid and false otherwise
		"""
		valid = True
		if self.boardX > x or x > self.boardSize + self.boardX:
			valid = False # check if the move is within the range of the board
		if self.boardY > y or y > self.boardSize + self.boardY:
			valid = False  # check if the move is within the range of the board		
		(x,y) =  self.convertCoordinate(1,(x,y))
		if board[y][x] == opponentTile or board[y][x] == playerTile:
			valid = False # check if there is already a tile on position x,y
		hasTile = False
		for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
			hasOpp = False
			goX = x
			goY = y
			goX  += xdirection
			goY += ydirection
			while self.onboard(goX,goY) and board[goY][goX] == opponentTile:	
				goX += xdirection
				goY += ydirection
				hasOpp = True 
			if hasOpp and self.onboard(goX,goY) and board[goY][goX] == playerTile :		
				hasTile = True # check if the move can trigger a flip of player's opponent's tile.
		return (valid and hasTile)

	def onboard(self,x, y):
		return x >= 0 and x <= 7 and y >= 0 and y <=7

	def convertCoordinate(self,parameter, tuplein):
		"""
		convertCoordinate converts the screen coordinate of a move to the board coordinate of a move and vice versa
		Args:
			parameter(int): when parameter equals 1, converts screen coordinate to board coordinate and do the opposite when it
			equals 0
			tuplein((x,y)): tuple representing the position of a move

		Returns:
			the converted coordinate
		"""
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

	def update_Text(self,reversi,yield_):
		"""
		updates the scores of both user and computer and the current status of the game

		Args:
			yield_(int): yield_ != 0 indicates that one player can not make a valid move at this round and play passes back to the other player

		Returns:
			end(boolean): true if game has reached its end and false otherwise
		"""

		pygame.draw.rect(self.screen, self.infoBoardColor,pygame.Rect(self.infoBoardx ,self.infoBoardy, self.infoBoardwidth, self.infoBoardheight)) 
		pygame.draw.rect(self.screen, self.infoBoardColor,pygame.Rect(self.infoBoardx ,self.infoBoardy + self.infoBoardheight + 20, self.infoBoardwidth,self.infoBoardheight))

		
		self.screen.blit(self.playerTileImage,(self.infoBoardx + 10,self.infoBoardy + 10)) # draw user tile on the info board. 
		self.screen.blit(self.computerTileImage,(self.infoBoardx + 10,self.infoBoardy + self.infoBoardheight + 20 + 10 )) # draw computer tile on the info board.

		userString = "You"
		computerString = "Computer" 

		userString = self.textFont.render(userString,True,self.fontColor)
		computerString = self.textFont.render(computerString,True,self.fontColor)
		self.screen.blit(userString,(self.infoBoardx + 70,self.infoBoardy + 30)) # write "You" on user's info board
		self.screen.blit(computerString,(self.infoBoardx + 70,self.infoBoardy + self.infoBoardheight + 20 + 30)) # write "Computer" on computer's info board.
		
		computerScore, userScore = reversi.getscore(self.userTile,self.computerTile)
		end = False
		end = self.endOfGame(computerScore, userScore) # checks if the game has ended
		
		userScoreString = "User Score: " + str(userScore)
		computerScoreString = "Computer score: " + str(computerScore)

		userScoreString = self.textFont.render(userScoreString,True,self.fontColor)
		computerScoreString = self.textFont.render(computerScoreString,True,self.fontColor)
		self.screen.blit(userScoreString,(self.infoBoardx + 10,self.infoBoardy + 80)) # updates user's score
		self.screen.blit(computerScoreString,(self.infoBoardx + 10,self.infoBoardy + self.infoBoardheight + 20 + 10 + 70)) # updates computer's score

		userPosString = "Current Position: " + str(self.userPos)
		computerPosString = "Current position: " + str(self.computerPos)

		userPosString = self.textFont.render(userPosString,True,self.fontColor)
		computerPosString = self.textFont.render(computerPosString,True,self.fontColor)
		self.screen.blit(userPosString,(self.infoBoardx + 10,self.infoBoardy + 120)) # update user's move
		self.screen.blit(computerPosString,(self.infoBoardx + 10,self.infoBoardy + self.infoBoardheight + 20 + 10 + 50 + 60)) # update computer's move

		endString = " "
		if end == True:
			print("computerScore",computerScore)
			print("userScore",userScore)
			if computerScore > userScore:
				endString = "The computer wins!"
			elif computerScore < userScore:
				endString = "The user wins!"
			elif computerScore == userScore:
				endString = "Both win!"
			yieldString = "Press R to restart."
			endString = self.textFont.render(endString,True,self.fontColor) # prompt user that the game has ended
			restartString = self.textFont.render(yieldString,True,self.fontColor) # prompt user to restart by pressing R key
			self.screen.blit(endString,(35,400))
			self.screen.blit(restartString,(25,440))

		else:
			yString = " "
			if yield_ == 1:
				yString = "Yield to User"
			elif yield_ == 2:
				yString = "Yield to Computer"
			yieldString = self.textFont.render(yString,True,self.fontColor) # prompt user that play is passed to user or computer
			self.screen.blit(yieldString,(35,400))

		return end

	def run_game(self,reversi):
		"""
			run_game controls the flow of the game
			
			Args:
				reversi(object): contains all functions necessary for running the game

			Returns:
				restart(boolean): true if user wants to restart the game and false otherwise
		"""
		restart = False
		end = False 

		board = reversi.getBoard() # initialize game board
		AI = Reversi_AI()

		end = self.drawBoard(reversi,0) # draw the game board
		yield_ = 0
		waitForComputer = False
		waitForUser = True # let user go first

		loop = True
		while loop:
			
			for event in pygame.event.get():			
				if end: # if end of the game
					print("end of this round")
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r:
							restart = True
							print("down key")
							loop = False # end the game 
				elif event.type is pygame.QUIT:
					sys.exit()	
				elif event.type is pygame.MOUSEBUTTONDOWN:
					(mouseX,mouseY) = pygame.mouse.get_pos()
					if waitForUser is True: # player's turn
						if len(AI.searchAllmoves(board,"X","0")) > 0:	# if there are valid moves for player 
							yield_ = 0		
							if self.checkValid(mouseX,mouseY,board,"X","0"): # if user chooses a valid move
								(userX,userY) = self.convertCoordinate(1,(mouseX,mouseY))
								self.updatePos(1,userX+1,userY+1)

								board = reversi.updateboard(userX,userY,self.userTile) # update board according to new move
								end = self.drawBoard(reversi,yield_)

								pygame.display.flip()
								pygame.time.wait(200)
								
								board = reversi.reverse(userX,userY,self.userTile,self.computerTile) # reverse tiles
								end = self.drawBoard(reversi,yield_)
								
								pygame.display.flip()
								pygame.time.wait(200)

								waitForComputer = True # computer's turn
								waitForUser = False
							else:
								print("invalid move")
						else: # if no valid move for player
							print("yield to computer")
							yield_ = 2
							waitForComputer = True # pass play to computer
							waitForUser = False
							

				elif waitForComputer is True: # computer's turn
					bestMove = reversi.searchbestmoves(self.computerTile, self.userTile) # get best move for computer
					if bestMove != None:
							yield_ = 0

							board = reversi.updateboard(bestMove[0],bestMove[1],self.computerTile)
							self.updatePos(0,bestMove[0]+1,bestMove[1]+1) # update board according to new move
							end = self.drawBoard(reversi,yield_) 

							pygame.display.flip()
							pygame.time.wait(200)
							print("waitForComputer")
						
							board = reversi.reverse(bestMove[0],bestMove[1],self.computerTile,self.userTile) # reverse tiles	 		
					else: 
						print("yield to user")
						yield_ = 1	 # pass play to computer
				 		
					waitForComputer  = False
					waitForUser = True
				 	
				else: # user has not clicked on the board at user's turn
					if len(AI.searchAllmoves(board,"X","0")) == 0:
						waitForComputer = True
						waitForUser = False
						yield_ = 2 # if no valid move for user, pass play to computer
						print("yield to computer")
						


				# update board

				end = self.drawBoard(reversi,yield_)
			pygame.display.flip()
			if yield_ != 0:
				pygame.time.wait(1000)
			else: 
				pygame.time.wait(200)
		print("out of the loop")
		return restart

	def start_game(self,reversi):
		"""
		start_game starts the reversi game and initializes a new game whenever user wants to continue to play
		"""
		restart = self.run_game(reversi)  
		while restart:
			print("here?")
			newReversi = Reversi()  # initialize reversi object    
			newReversi.initiateboard() # initialize the game board
			restart = self.run_game(newReversi)
		print("goodbye!")

if __name__ == "__main__":
	
    reversi = Reversi()  # initialize reversi object    
    computertile = reversi.assigntile('X') # assign string 'X' to be computer's tile
    reversi.initiateboard() # initialize the game board
    game = Reversi_GUI() # initialize the GUI for Reversi
    game.start_game(reversi) # start the game
    

