
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
		
	
	
	print('Initial page ranks:')
	print(page_ranks)
	
	for _ in range(100):
		for j in range(size):
			temp = 0
			for i in range(size):
				if outlinks[i][j] == 1:
					temp += page_ranks[i] / out_degrees[i]
			temp *= d
			temp += (1-d)
			page_ranks[j] = round(temp, 4)
		
	return page_ranks
			
outlinks = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0]
outlinks = np.reshape(outlinks, (5, 5))
page_ranks = calculate_PageRank(outlinks)	
print()
print('The converged page rank is:')
print(page_ranks)
print()
sums = 0
for i in page_ranks:
	sums += i
print('The sum of page ranks is: ', round(sums, 4))
