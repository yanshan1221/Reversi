# Implementation of the Alpha-Beta Pruning.
# Does not set value of node. 
# take in a min max tree and return the root value through propagation.


from Min_Max_Tree import Min_Max_Tree

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

# Testing.
if __name__ == "__main__":

 	root = Min_Max_Tree("min")
 	node1 = Min_Max_Tree("max")
 	node2 = Min_Max_Tree("max")
 	
 	root.addNode(node1)
 	root.addNode(node2)

 	node4 = Min_Max_Tree("min")
 	node5 = Min_Max_Tree("min")
 	node6 = Min_Max_Tree("min")

 	node7 = Min_Max_Tree("max")
 	node8 = Min_Max_Tree("max")

 	node1.addNode(node4)
 	node1.addNode(node5)
 	node1.addNode(node6)

 	node5.setValue(4) 
 	node6.setValue(0)

 	node4.addNode(node7)
 	node4.addNode(node8)


 	node7.setValue(1)
 	node8.setValue(2)

 	node9 = Min_Max_Tree("min")
 	node10 = Min_Max_Tree("min")

 	node9.setValue(5)
 	node10.setValue(2)

 	node2.addNode(node9)
 	node2.addNode(node10)

 	finalVal = Alpha_Beta(root,float('-inf'),float('inf'))
 	print finalVal
 	

