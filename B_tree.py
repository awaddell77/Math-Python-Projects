#bin tree


class B_tree:
	def __init__(self, head):
		self.head = head
	def add(self, data):
		root = self.head
		if not root:
			self.head = Node(data)
			return
		return self._add_help(data, root)
		
	def _add_help(self, data, node):
		
		#needs to control for insertions/duplicates

		if not node:
			return Node(data)
		if data == node.data: return node
		print(node.data)
		#if not node.left and not node.right and data < node.data:
			##node.left = Node(data)
			#return node
		#elif not node.left and not node.right and data> node.data:
			#node.right = Node(data)
			#return node
		if data > node.data:
			node.right =self._add_help(data, node.right)
			return node
		if data < node.data:
			node.left = self._add_help(data, node.left)
			return node

		return node




			

	def _travel(self, data, node):
		print("NODE IS {0}".format(node.data))
		if not node: return node
		if data == node.data: return node
		if data < node.data and node.left:

			 return self._travel(data, node.left)
		elif data < node.data and not node.left:
			return node
		if data > node.data and node.right:
			return self._travel(data, node.right)
		elif data > node.data and not node.right:
			return node 
		#return node
	def find(self, data):
		#if it cannot find a node with the given data it will return the last node traversed
		node = self.head
		return self._travel(data, node)





class Node:
	def __init__(self,data):
		self.data = data
		self.left = ''
		self.right = ''
	def __str__(self):
		return "D:" + str(self.data) + "L:"+str(self.left) + " R:"+ str(self.right)
n1 = Node(5)
'''n2 = Node(1)
n3 = Node(3)
n4 = Node(4)
n1.right = n4
n1.left = n3
n3.left = n2'''
tst_tree = B_tree(n1)