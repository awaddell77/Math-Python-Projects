import time
def sum_to_num(num):
	total = 0
	start = time.time()
	for i in range(0, num+1):
		#print("Adding ", str(i))
		total += i
	duration = time.time() - start
	print("Took {0} seconds".format(duration))
	return total
def primes_to_num(num):
	#intentionally o(n^2)
	start = time.time()
	primes = []
	for i in range(1, num+1):
		prime_flag = False
		for i_2 in range(1, i):
			if  i % i_2 == 0 and i_2 != 1: break
			if i_2 == i-1: primes.append(i)
	duration = time.time() - start
	print("Took {0} seconds".format(duration))
	return primes


def num_of_primes(num):
	#intentionally o(n^2)
	start = time.time()
	cnt= 0
	primes = []
	for i in range(1, num+1):
		prime_flag = False
		for i_2 in range(1, i):
			if  i % i_2 == 0 and i_2 != 1: break
			if i_2 == i-1: cnt += 1
	duration = time.time() - start
	print("Found {0} prime numbers".format(cnt))
	print("Took {0} seconds".format(duration))
	

number = sum_to_num(1000000)
print("Number: ", str(number))
#primes = primes_to_num(1000)
num_of_primes(1000)
#print("Primes:")
#print(primes)

