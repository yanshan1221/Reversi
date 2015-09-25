# A class of general Tree, where each node has its leaves stored in a list of objects.
# If the node is min node than its pos value is 0 and 1 otherwise.
# A DFS algorithm for printing nodes.

class Min_Max_Tree:
 	def __init__(self,pos):
 		self.value = None
 		self.next = []
 		if pos:
 			self.pos = "min"
 		else:
 			self.pos = "max"

 	def addNode(self,node):
 		self.next.append(node)

 	def Pos(self):
 		return self.pos

 	def Next(self):
 		return self.next

 	def setValue(self,object):
 		self.value = object

 	def deleteNode(self,node):
 		self.next.remove(node)

 	def Value(self):
 		return self.value

 	def printTree(self,node):
 		print node.Value()
 		if node.next == []:
 			return
 		else:
 			for n in node.Next():
 				n.printTree(n)
 				


# Testing.
if __name__ == "__main__":

 	root = Min_Max_Tree("min")
 	node1 = Min_Max_Tree("max")
 	node2 = Min_Max_Tree("max")
 	root.setValue(0)
 	node2.setValue(1) 
 	node1.setValue(2) 
 	root.addNode(node1)
 	root.addNode(node2)

 	root.printTree(root)
