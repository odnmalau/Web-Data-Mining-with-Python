
import numpy as np


def calculate_PageRank(outlinks):
	
	
	
	d = 0.85
	
	
	size = outlinks.shape[0]
	
	
	page_ranks = [1 for i in range(size)]
	
	
	out_degrees = []
	for i in range(size):
		sums = 0
		for j in range(size):
			sums += outlinks[i][j]
		out_degrees.append(sums)
		
	
	in_degrees = []
	for j in range(5):
		sums = 0
		for i in range(5):
			sums += outlinks[i][j]
		in_degrees.append(sums)
		
	
	
	
	print('Initial page ranks:')
	print(page_ranks)

	
	nodes = {}
	for i in range(5):
		temp = []
		for j in range(5):
			if outlinks[i][j] == 1:
				temp.append(j)
		nodes[i] = temp

	

	for _ in range(100):
		for j in range(size):
			temp = 0
			for i in range(size):
				out_degree = 0
				in_degree = 0
				if outlinks[i][j] == 1:
					for l in nodes[i]:
						out_degree += out_degrees[l]
						in_degree += in_degrees[l]
					temp += page_ranks[i] * (in_degrees[j] / in_degree) * (out_degrees[j] / out_degree)
			temp *= d
			temp += (1 - d)
			page_ranks[j] = round(temp, 4)
		
	return page_ranks
			
outlinks = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
outlinks = np.reshape(outlinks, (5, 5))
page_ranks = calculate_PageRank(outlinks)
print()	
print('The converged weighted page rank is:')
print(page_ranks)
sums = 0
for i in page_ranks:
	sums += i
print('\nThe sum of weighted page ranks is: ', round(sums, 4))
