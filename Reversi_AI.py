from Alpha_Beta import Alpha_Beta
from Reversi import Reversi
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
						print("C")
						# X positions
					elif (i,j) in [(1,1),(1,6),(6,1),(6,6)]:
						weight = self.Xweight
						print("X")
						# Corners	
					elif (i,j) in [(0,0),(7,7),(0,7),(7,0)]:
						weight = self.cornerWeight
						print("Corner")
					if board[i][j] == tile:
						
						score = weight + score
						print(score)
					else:
						score = weight * (-1) + score
		nextMoves = self.searchAllmoves(board,tile,oppositetile)
		mobility = len(nextMoves)
		print("mobility",mobility)
		score = score + mobility
		return score 

	#  m = True for min, false for max.
	def generateTree(self,board,depth,m,tile,oppositetile):

		node = Min_Max_Tree(m)
		# when finish all the lookups. 
		if depth == 0:
			score = self.f_s(board,"X","0")
			node.setValue(score)
			print(board, "with score",score)
			return node
		# logic
		else:
			# a list of moves
			moves = self.searchAllmoves(board,tile,oppositetile)
			for move in moves:
				board = self.updateBoard(board,move,tile,oppositetile)
				child = self.generateTree(board,depth - 1,not m,oppositetile,tile)
				node.addNode(child)

			return node

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
				
	
	def updateBoard(self,board,move,tile,oppositetile):
		y = move[1]
		x = move[0]
		board[y][x] = tile
		board = self.reverse(x,y,tile,oppositetile)
		return board

	def reverse(self,initx,inity,tile,oppositetile):

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
	def getBestMove(self,board,depth,tile,oppositetile):
		m = False # this is equivalent to "max".
		possibleMoves = self.searchAllmoves(board,tile,oppositetile)
		
		bestMove = None
		bestScore = 0
		if len(possibleMoves) > 0:
			for move in possibleMoves:
				board = self.updateBoard(board,move,tile,oppositetile)
				
				root = self.generateTree(board,depth,m,oppositetile,tile)
			
				alpha, beta = float("-inf"),float("inf")
				new = self.Alpha_Beta(root, alpha, beta)
				
				if  new > bestScore:
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
	(x,y) = reversi_AI.getBestMove(board,2,"X","0")

	print (x,y)




 












