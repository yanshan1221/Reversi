# Given a min_max Tree with all leafs value known, obtain all values of the rest of tree through propagation. 
# It is DFS algorithm.

from Reversi import Reversi
from Min_Max_Tree import Min_Max_Tree

def minMax_Search(node):
	
	if node.Next() == []:	
		return node.Value()
	else:
		if node.Pos() is "min":
			best = float('inf')
			for next in node.Next():
				best = min(best,minMax_Search(next))	
			node.setValue(best)	
			
		elif node.Pos() is "max":
			best = float('-inf')
			for next in node.Next():
				best = max(best,minMax_Search(next))			
			node.setValue(best)
		
		return best
				


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

 	node5.setValue(3) 
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

 	minMax_Search(root)
 	root.printTree(root)
 	
 	print "root value is", root.Value()
 	

