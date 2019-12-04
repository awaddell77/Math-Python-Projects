#bin tree

#technically it is a binary search tree
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
	def remove(self, data):
		root = self.head
		self._remove_help(data, root)
		return

	def _remove_help(self, data, node):
		if node.right.data == data and node.right.right:
			node.right = node.right.right
			node.right.left = node.right.left #this is wrong
			return 
		#if data == node.data: return node
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
	def print_tree(self):
		self._traverse(self.head, 1)
		
	def _traverse(self, node, depth):
		#inorder traversal (left, root, right)
		if not node: return
		#print("NODE IS {0}".format(node.data))
		
		depth += 5
		

		self._traverse(node.left, depth)
		#operation goes here
		print(str(node.data), end='')
		
		self._traverse(node.right, depth)
		#print((' ' * depth) + str(node.data), end='')








class Node:
	def __init__(self,data):
		self.data = data
		self.left = ''
		self.right = ''
	def __str__(self):
		return "D: " + str(self.data) +"[" + "L: "+str(self.left) + " R: "+ str(self.right) +"]"
	def __repr__(self):
		return self.__str__()
n1 = Node(10)
'''n2 = Node(1)
n3 = Node(3)
n4 = Node(4)
n1.right = n4
n1.left = n3
n3.left = n2'''
tst_tree = B_tree(n1)
tst_tree.add(20)
tst_tree.add(8)
tst_tree.add(4)
tst_tree.add(25)
tst_tree.add(13)
tst_tree.add(6)
tst_tree.add(3)
tst_tree.print_tree()