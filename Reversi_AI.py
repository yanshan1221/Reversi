from Alpha_Beta import Alpha_Beta
from Min_Max_Tree import Min_Max_Tree

# The configuration of a specific board is denoted here as s. 

class Reversi_AI:
	def __init__(self):
		# setting all weights in the constructor.
		self.Cweight = -3
		self.Xweight = -5
		self.cornerWeight = 3
	
	def onboard(self,x, y):
		return x >= 0 and x <= 7 and y >= 0 and y <=7

	# return a set of valid moves for a m parent configuration
	def searchAllmoves(self,board,tile,oppositetile):

        # First, get a list of positions of computer's tiles on the board.
		tilelist = []
		for i in range(8):
			for j in range(8):
				if board[i][j] == tile:
					tilelist.append([j,i])
                   #  Set the largest number of usertiles that can be flipped to zero.
                   #  Set the best move's horizontal position to be -1 and its vertical position to be -1.
		largenumflipped = 0
		bestx = -1
		besy = -1

        # for each computer's tile on the board, search in eight directions for the possible next move.
		possibleMoves = []
		for i in range(len(tilelist)):
			initx = tilelist[i][0]
			inity = tilelist[i][1]
            
			for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
				x = initx
				y = inity
				x += xdirection
				y += ydirection
                # Moves that can cause user's tiles to be reversed are better than those that can't help increase the score of the computer.Hence only continuing the while
                # loop if there is user's tile around.
				while self.onboard(x,y) and board[y][x] == oppositetile :
					x += xdirection
					y += ydirection
                    #  When the while loop above stops, we get the x, y of the possible moves. If its position is on the board and also unoccupied, then count the number of user's tiles that can be flipped.   
				if self.onboard(x,y) and board[y][x] == " ":
					# dealing the case when there is no opposite tile around the tile. 
					if abs(x -  tilelist[i][0]) > 1 or abs(y - tilelist[i][1]) > 1:
						if (x,y) not in possibleMoves:
							possibleMoves.append((x,y))
        
        # When no move is valid, that means no move can possibly cause a flip of opponent's tile, in this case, whoever is playing 
        # this round will have to yield to its opponent. 
		return possibleMoves	

	# the evaluation function that assign a value to a possible configuration. 
	# f_eval = s[i,j] * weight[i,j] + Mobility[tile]
	def f_s(self,board, tile, oppositetile):
		# we give certain positions on board higher scores than other positions, 
		score = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				# at position (i,j)
				if board[i][j] != " ":
					weight = 1
					# C positions
					if (i,j) in [(0,1),(0,6),(1,0),(1,7),(6,0),(7,1),(6,7),(7,6)]:
						weight = self.Cweight
						# X positions
					elif (i,j) in [(1,1),(1,6),(6,1),(6,6)]:
						weight = self.Xweight	
						# Corners	
					elif (i,j) in [(0,0),(7,7),(0,7),(7,0)]:
						weight = self.cornerWeight	
					if board[i][j] == tile:
						score = weight + score
						
					else:
						score = weight * (-1) + score
		nextMoves = self.searchAllmoves(board,tile,oppositetile)
		mobility = len(nextMoves)
		score = score + mobility
		return score 

	def drawboard(self,board):
		print "   1   2   3   4   5   6   7   8"
		horline = " .___.___.___.___.___.___.___.___."
		verline = "|   |   |   |   |   |   |   |   | "
		print horline 
		for i in range(8):
			print " %s" %verline  
			print str(i + 1) + verline
			for j in range(8):
				print " |%s"% board[i][j],
			print " |"
			print horline

	#  m = True for min, false for max.
	def generateTree(self,board,depth,m,tile,oppositetile,alpha,beta):
		#self.drawboard(board)
		#print tile
		#node = Min_Max_Tree(m)
		# when finish all the lookups. 
		if depth == 0:
			score = self.f_s(board,"X","0")
			#node.setValue(score)
			#print(score)
			return score
		# logic
		else:
			# a list of moves
			moves = self.searchAllmoves(board,tile,oppositetile)
			childValue  = 0
			if len(moves) > 0:
				for move in moves:
					newBoard = self.updateBoardRepresentation(board,move,tile,oppositetile) #self.drawboard(newBoard)
					childValue = self.generateTree(newBoard,depth - 1,not m,oppositetile,tile,alpha,beta)
			else:
				childValue = self.generateTree(board,depth-1,not m,oppositetile,tile,alpha,beta)

			if m:
				if childValue < beta:
					beta = childValue
				return beta
			elif not m:
				if childValue > alpha:
					alpha = childValue
				return alpha
			


	# execute the alpha beta pruning of the min max tree. 
	def Alpha_Beta(self,node, alpha, beta):
		if alpha >= beta:
			return 1

		elif node.Next() == []:	
			return node.Value()

		else:
			if node.Pos() is "max":
				for next in node.Next():
					k = Alpha_Beta(next,alpha,beta) 
					if k > alpha:
						alpha = k
				return alpha
				#node.setValue(best)				
			elif node.Pos() is "min":
				for next in node.Next():
					m = Alpha_Beta(next,alpha,beta)	
					if m < beta:
						beta = m
				return beta
		
				#node.setValue(best)
				
	# changed the updateBoard function
	def updateBoardRepresentation(self,board,move,tile,oppositetile):
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
		newBoard[y][x] = tile
		newBoard = self.reverseRep(newBoard,x,y,tile,oppositetile)
		return newBoard

	# changed reverse function
	def reverseRep(self,board,initx,inity,tile,oppositetile):

        # for the new tile, search in eight directions for its oppositetile.
        
		for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
			x = initx
			y = inity
			x += xdirection
			y += ydirection
        
			while self.onboard(x,y) and board[y][x] == oppositetile:
				x += xdirection
				y += ydirection
                    # keep incrementing both the x and y position of the new tile till it meets the tile of its own type.
			if self.onboard(x,y) and board[y][x] == tile:
				x -= xdirection
				y -= ydirection
                # going backwards and reverse all the opposite tiles in between.
				while self.onboard(x,y) and board[y][x] == oppositetile:
					
					board[y][x] = tile
					x -= xdirection
					y -= ydirection
                    # return the new board.
		return board


	# we lose the data about possible moves in the tree. 
	# This function will return None when the searchAllmoves function has length 0. 
	def getBestMove(self,board,depth,tile,oppositetile):
		m = False # this is equivalent to "max".
		possibleMoves = self.searchAllmoves(board,tile,oppositetile)
		#print(possibleMoves)
		bestMove = None
		bestScore = float("-inf")
		if len(possibleMoves) > 0:
			for move in possibleMoves:
				newBoard = self.updateBoardRepresentation(board,move,tile,oppositetile)
				alpha, beta = float("-inf"),float("inf")
				new = self.generateTree(newBoard,depth,m,oppositetile,tile,alpha,beta)
				#print(new)
				#new = self.Alpha_Beta(root, alpha, beta)	
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
	#testPossibleMoves = reversi_AI.searchAllmoves(board,'X','0')
	#for move in testPossibleMoves:
		#print "Testing For searchAllmoves:", move

	# Testing for f_s
	#scoreR = reversi_AI.f_s(board,"X","0")
	#print "Testin for f_s", scoreR

	(x,y) = reversi_AI.getBestMove(board,5,"X","0")

	print (x,y)




 












