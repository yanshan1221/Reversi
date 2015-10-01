# A class of general Tree, where each node has its leaves stored in a list of objects.

class Tree:
 	def __init__(self):
 		self.value = None
 		self.next = []

 	def addNode(self,node):
 		self.next.append(node)

 	def Next(self):
 		return self.next

 	def setValue(self,object):
 		self.value = object

 	def deleteNode(self,node):
 		self.next.remove(node)

 	def Value(self):
 		return self.value

if __name__ == "__main__":

 	root = Tree()
 	node1 = Tree()
 	node2 = Tree()
 	node2.setValue(1) 
 	node1.setValue(2) 
 	root.addNode(node1)
 	root.addNode(node2)

 	list = root.Next()
 	for item in list:
 		print item.Value()
main()