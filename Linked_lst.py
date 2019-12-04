#linked list


class Linked_lst:
	def __init__(self, head):
		self.head = head
	def add_last(self, data):
		temp = self.head
		while True:
			if not temp.next:
				temp.next = Node(data)
				break
			


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
