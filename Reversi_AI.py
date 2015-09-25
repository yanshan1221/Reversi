from alpha-Beta import alpha-Beta
from Reversi import Reversi

# The configuration of a specific board is denoted here as s. 


class Reversi_AI:
	def __init__(self):
		self.a = 0

	# have to write recursion again if you do not want to save the information about the board = =
	# S is the set of all con

	# return a set of valid moves for a m parent configuration
	def generateMoves(board):
		validMoves = []


		return validMoves
	# the evaluation function that assign a value to a possible configuration. 
	def f_s(board):
		score = 0

		return score 
	#  m = True for min, false for max
	def generateTree(self,board,depth,m):
		node = Min_Max_Tree(m)
		# when finish all the lookups. 
		if depth == 0:
			score = self.f_s(board)
			node.setValue(score)
			return node
		# logic
		else:
			# a list of moves
			moves = self.generateMoves(board)
			for move in moves:
				board = self.updateBoard(board,move)
				child = self.generateTree(board,depth - 1,not m)
				node.Next = child

			return node
	def Alpha_Beta(node, alpha, beta):
		if alpha >= beta:
			return

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
				
	# we lose the data about possible moves in the tree. 

	def getBestMove(self,board,depth,):
		m = "min"
		root = self.generateTree(board,depth,m)
		alpha, beta = float(-inf),float(inf)
		bestMove = None
		bestScore = 0
		for possible in root.Next():
			if self.Alpha_Beta(possible, alpha, beta) > bestScore:
				bestScore = self.Alpha_Beta(possible, alpha, beta)
				bestMove = possible

		return possible















