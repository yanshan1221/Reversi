from Min_Max_Tree import Min_Max_Tree

"""
	Reversi_AI is the class that creates Reversi_AI objects that can decide
	the best move for a player using min-max tree algorithm with alpha-beta pruning.
"""

class Reversi_AI:
	"""
   Reversi_AI is an AI Class for the Reversi Game, which contains all AI functions for Reversi.
   
   Attributes:
      Cweight(int): the weight for C postions on the board
      Xweight(int): the weight for X positions on the board
      cornerWeight(int): the weight for corners
	"""
	def __init__(self):
		
		self.Cweight = -3
		self.Xweight = -5
		self.cornerWeight = 3
	
	def onboard(self,x, y):
		""" 
		check if position (x,y) is on the board.
		    
		Args: 
		    x(int): The x coordinate on the board.
			y(int): The y coordinate on the board. 
			
		Returns:
		    True if the (x,y) is within the board range, otherwise False
		"""
		return x >= 0 and x <= 7 and y >= 0 and y <=7

	def searchAllmoves(self,board,playerTile,opponentTile):
		"""
		searchAllmoves search for all positions on the game board where whoever(user/computer) is playing in this round could place his tile.

		Args:
		    board(int[][]): board configuration stored in a 2-D array.
		    playerTile(string): string that represents user/computer's a tile
		    opponentTile(string): string that represents a tile of opposite color
		
		Returns:
		    AllPossibleMoves([]):a list of all possible moves (x,y) for whoever is playing in this round. 
		"""
		tilelist = []
		# obtain a list of all positions occupied by player's tile.
		for i in range(8):
			for j in range(8):
				if board[i][j] == playerTile:
					tilelist.append([j,i])

		largenumflipped = 0 #  Set the largest number of players' tiles that can be flipped to zero.
		bestx, besy = -1, -1 #  Set the best move's horizontal position to be -1 and its vertical position to be -1.

		possibleMoves = []
		# for each player's tile on the board, search in eight directions for the possible next move.
		for i in range(len(tilelist)):
			initx = tilelist[i][0]
			inity = tilelist[i][1]
            
			for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
				x = initx
				y = inity
				x += xdirection
				y += ydirection

				while self.onboard(x,y) and board[y][x] == opponentTile :
					# game rule only allows player to place tiles at postions 
					# where flip of opponent's tile is guaranteed.
					x += xdirection
					y += ydirection
					
				if self.onboard(x,y) and board[y][x] == " ":
					# dealing the case when there is no opposite tile around the tile. 
					if abs(x -  tilelist[i][0]) > 1 or abs(y - tilelist[i][1]) > 1:
						if (x,y) not in possibleMoves:
							possibleMoves.append((x,y))
		return possibleMoves	

	def f_s(self,board,playerTile,opponentTile):
		"""
		f_s evaluates the score of a given board configuration based on the formula: 
		f(board) = board[i,j] * weight(i,j) + Mobility[playerTile]

		Args: 
		   board(int[][]): 2-D array representation of the game board configuration.
		   playerTile(str): A string that represents player's tile 
		   opponentTile(str): A string that represents oppponent's tile

		Returns:
		   sore(int): A evaluated score for a given board configuration.
		"""		
		score = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] != " ":
					weight = 1
					if (i,j) in [(0,1),(0,6),(1,0),(1,7),(6,0),(7,1),(6,7),(7,6)]:
						weight = self.Cweight # C positions
					elif (i,j) in [(1,1),(1,6),(6,1),(6,6)]:
						weight = self.Xweight	# X positions
					elif (i,j) in [(0,0),(7,7),(0,7),(7,0)]:
						weight = self.cornerWeight # Corners	
					if board[i][j] == playerTile:
						score += weight # player's tile
					else:
						score -= weight  # opponent's tile		
		nextMoves = self.searchAllmoves(board,playerTile,opponentTile)
		mobility = len(nextMoves)
		score = score + mobility
		return score 


	def generateTree(self,board,depth,m,playerTile,opponentTile,alpha,beta):
	#  m = True for min, false for max.
		"""
		generateTree generates a min-max tree with alpha-beta pruning, given an initial game board configuraiton.
		
		Args:
		   board(int[][]): 2-D array representing the game board configuration.
		   depth(int): the depth of the min-max tree.
		   alpha(int): the alpha value for alpha beta pruning
		   beta(int): the beta value for alpha beta pruning
		   playerTile(str): A string that represents player's tile
		   opponentTile(str): A string that represents player's opponent's tile
		   m(boolean): True for min state and False for max state

		Returns:
		   The value assigned to the root node of the min-max tree
		"""
		if depth == 0:
			score = self.f_s(board,"X","0")
			return score
		else:
			moves = self.searchAllmoves(board,playerTile,opponentTile) # a list of possible moves for player.
			childValue  = 0
			if len(moves) > 0:
				for move in moves:
					newBoard = self.updateBoardRepresentation(board,move,playerTile,opponentTile) # suppose player places a tile according to move, update the board
					childValue = self.generateTree(newBoard,depth - 1,not m,opponentTile,playerTile,alpha,beta)
			else:
				childValue = self.generateTree(board,depth-1,not m,opponentTile,playerTile,alpha,beta)
				
			# alpha-beta pruning
			if m:
				if childValue < beta:
					beta = childValue
				return beta
			elif not m:
				if childValue > alpha:
					alpha = childValue
				return alpha
			
	def updateBoardRepresentation(self,board,move,playerTile,opponentTile):
		"""
		updateBoardRepresentation updates the board configuration by placing a tile according to player's move

		Args:
		   board(int[][]): 2-D array that stores the board configuration
		   move((x,y)): a tuple that represents the x,y coordinate of the position of player's move.
		   playerTile(str): a string that represents player's tile
		   opponentTile(str): a string that represents opponent's tile.

		Returns:
		   An updated board configuration
		"""
		newBoard = []
		for i in range(8):
			newBoard.append([" "]*8)
		for i in range(8):
			for j in range(8):
				newBoard[i][j] = " " 
		for i in range(8):
			for j in range(8):
				newBoard[i][j] = board[i][j]
		y = move[1]
		x = move[0]
		newBoard[y][x] = playerTile
		newBoard = self.reverseRep(newBoard,x,y,playerTile,opponentTile)
		return newBoard

	
	def reverseRep(self,board,initx,inity,playerTile,opponentTile):
		"""
		reverseRep is a helper function for updateBoardRepresentation which reverses all tiles in between
		two tiles of the player, while one of them is a newly placed on board.

		Args:
		   board(int[][]): a 2-D board configuration
		   initx(int): the x coordinate of player's new move
		   inity(int): the y coordinate of player's new move
		   playerTile(str): a string that represents player's tile
		   opponentTile(str): a string that represents opponent's tile.
		   
		Returns:
		   A updated board configuration that has reversed all tiles in between two tiles of player, while one
		   is the most recent move of the player.
		"""
		for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		#search in eight directions for the opponent's tiles.
			x = initx
			y = inity
			x += xdirection
			y += ydirection
        
			while self.onboard(x,y) and board[y][x] == opponentTile:
				x += xdirection
				y += ydirection
			if self.onboard(x,y) and board[y][x] == playerTile:
				# keep incrementing x and y till (x,y) is occupied by opponent's tile.
				x -= xdirection
				y -= ydirection
				while self.onboard(x,y) and board[y][x] == opponentTile:
					# going backwards while reversing all of opponent's tiles.
					board[y][x] = playerTile
					x -= xdirection
					y -= ydirection
		return board

	def getBestMove(self,board,depth,playerTile,opponentTile):
		"""
		getBestMove returns the best move computed by obtaining the best root value of the min-max tree.

		Args:
		   board(int[][]): 2-D array that stores the board configuration
		   depth(int): depth of the min-max tree
		   playerTile(str): a stirng that represents player's tile
		   opponentTile(str): a string that represents opponent's tile

		Returns:
		   the best move (x,y) for player computed by the min-max tree algorithm and
		   returns None if no such move exits
		   
		"""
		m = False # setting m to be "max".
		possibleMoves = self.searchAllmoves(board,playerTile,opponentTile)
		bestMove = None
		bestScore = float("-inf")
		if len(possibleMoves) > 0:
			for move in possibleMoves:
				newBoard = self.updateBoardRepresentation(board,move,playerTile,opponentTile)
				alpha, beta = float("-inf"),float("inf")
				new = self.generateTree(newBoard,depth,m,opponentTile,playerTile,alpha,beta)
				if  new >= bestScore:
					bestScore = new
					bestMove = move
		return bestMove


# Testing
if __name__ == "__main__":

	reversi_AI = Reversi_AI()	
	usertile = "X"
	computerTile = "0"
	board =[]
	for i in range(8):
		board.append([" "]*8)  
	for i in range(8):
		for j in range(8):
			board[i][j] = " "

	board[3][3] = 'X'
	board[3][4] = '0'
	board[4][3] = '0' 
	board[4][4] = 'X'

	board[1][1] = 'X'
	board[0][1] = '0' 
	board[1][0] = 'X'
	board[0][0] = '0'

	# Testing for Search ALl Moves:
	testPossibleMoves = reversi_AI.searchAllmoves(board,'X','0')
	for move in testPossibleMoves:
		print "Testing For searchAllmoves:", move

	# Testing for f_s
	scoreR = reversi_AI.f_s(board,"X","0")
	print "Testin for f_s", scoreR

	(x,y) = reversi_AI.getBestMove(board,5,"X","0")

	print (x,y)




 












