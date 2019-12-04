import random


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def rand_str(s_len):
	word = ''
	for i in range(0, s_len):word += chr(random.randint(97,122))
	return word





def hash_c(data):
	temp = 1
	for i in range(0, len(data)):
		temp *= ord(data[i]) + i
	return temp


lst = []
dup_st, hash_codes, collisions = set(), set(), 0
word_amount, hash_table_len = 200, 400
test_word = rand_str(6)
while True: 
	dup_st.add(rand_str(6))
	if len(dup_st) >= word_amount: break
val_lst = list(dup_st)
for word in val_lst:
	temp = hash_c(word)
	if temp in hash_codes: collisions += 1
	else: hash_codes.add(temp)
print("Out of {0} unique words, there were {1} collisions".format(len(val_lst), collisions))
print(test_word)