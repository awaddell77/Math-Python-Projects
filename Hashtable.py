
#hashtable
import random, time
class HashTable:
	def __init__(self, initial_arr_size):
		if not initial_arr_size: raise ValueError("Initial Array size cannot be zero")
	
		self._data_arr = [Node('') for i in range(0, initial_arr_size | 1)]
		self.size = initial_arr_size |1
		self.elem_num = 0
		self.slots_taken = 0
		self._load = .10
		self.collisions = 0
	def __repr__(self):
		disp_str = ''
		for i in range(0, len(self._data_arr)):
			#should add to list and .join them together with a ','
			temp = self._data_arr[i]
			if not temp.data: continue
			disp_str += str(temp.data) + ', '
			if temp.next:
				while True:
					temp = temp.next
					disp_str += str(temp.data) + ', '
					if not temp.next: break
		return disp_str
	def add(self, data):
		if self.elem_num / self.size >= self._load: 
			self._resize()
			
		temp_loc = self.hash_c(data) % self.size
		print("Index is {0}".format(temp_loc))
		temp_node = self._data_arr[temp_loc]
		if not temp_node.data: 
			self._data_arr[temp_loc].data = data
			self.elem_num += 1
			self.slots_taken += 1

			return
		if temp_node and temp_node.data == data: return
		else:
			temp = temp_node
			while True:
				if not temp.next: 

					temp.next = Node(data)
					print("Collision: {0} was already in the slot where {1} was supposed to go ".format(temp.data, data))
					self.elem_num += 1
					self.collisions += 1
					return
				temp = temp.next

				if temp.data == data: return
	def _resize(self):
		print("Resizing because {0} / {1} is >= {2}".format(self.elem_num, self.size, self._load))
		
		self.size = (self.size * 2) | 1

		
		self.elem_num, self.slots_taken = 0,0
		n_arr = [Node('') for i in range(0, self.size)]
		for i in range(0, len(self._data_arr)):
			temp = self._data_arr[i]
			self._resize_add(temp.data, n_arr)
			if temp.next:
				temp = temp.next
				while True:
					
					if not temp: break
					print("Resize: Adding {0}".format(temp.data))
					self._resize_add(temp.data, n_arr)
					temp = temp.next
		self._data_arr = n_arr
	def _resize_add(self, data, n_arr):
		if not data: return
		temp_loc = self.hash_c(data) % self.size
		print("Index is {0} for {1}".format(temp_loc, data))
		temp_node = n_arr[temp_loc]
		if not temp_node.data: 
			n_arr[temp_loc].data = data
			self.elem_num += 1
			self.slots_taken += 1

			return
		if temp_node and temp_node.data == data: return
		else:
			temp = temp_node
			while True:
				if not temp.next: 
					temp.next = Node(data)
					self.elem_num += 1

					return
				temp = temp.next

				if temp.data == data: return
	def is_in(self, key):
		h_key_index = self.hash_c(key) %self.size
		temp = self._data_arr[h_key_index]
		if temp.next:
			while True:
				if temp.data == key: return True
				temp = temp.next
				if not temp: return False
		return temp.data == key

		




	def get_index(self, num):
		return self._data_arr[num]



		


	def hash_c(self, data):
		temp = 0
		for i in range(0, len(data)):
			#temp *= (ord(data[i]) + i) + (ord(data[i])**(i + 1)) #bad
			#temp += (ord(data[i]) + i) + (ord(data[i])**(i + 1)) #better
			temp += ((ord(data[i]) + i) << 6 ) + ((ord(data[i])**(i + 1)) << 2) #best
		return temp

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def __repr__(self):
		return str(self.data)
def pr_node_chain(self, node):
	while True:
		if node:
			print(node)
			node = node.next
		else: return
def rand_str(s_len):
	word = ''
	for i in range(0, s_len):word += chr(random.randint(97,122))
	return word

tst_t = HashTable(200)
rec_lst = []
#tst_t.add('hello')
#tst_t.add('Numeral')
#tst_t.add('Num eral')
#tst_t.add('Numeral')
for i in range(0, 100):
	#print('looooooool') 
	word = rand_str(7)
	rec_lst.append(word)
	tst_t.add(word)
'''for i in range(0, 100):
	print('looooooool') 
	tst_t.add(rand_str(7))'''
print("Detected {0} collisions".format(tst_t.collisions))
t_word = rec_lst[random.randint(0, len(rec_lst)-1)] 
start = time.time()
res = rec_lst.index(t_word)
end = time.time()
print("Took {0} seconds to find {1}".format(end - start, t_word))
start = time.time()
tst_t.is_in(t_word)
end = time.time()
print("Took {0} seconds".format(end - start))