

import numpy as np
import os
import pickle


def authority_hub_score(outlinks):
	
	
	
	size = outlinks.shape[0]
	
	
	hub_scores = [1.0 for i in range(size)]
	authority_scores = [1.0 for i in range(size)]
	
	
	print(hub_scores)
	
	for _ in range(100):
		
		for j in range(size):
			temp_auth = 0.0
			for i in range(size):
				if outlinks[i][j] == 1:
					temp_auth += hub_scores[i]
			authority_scores[j] = temp_auth
			
		
		auth_sum = sum(authority_scores)
		
		for i in range(len(authority_scores)):
			authority_scores[i] /= auth_sum
		
		
		for i in range(size):
			temp_hub = 0.0
			for j in range(size):
				if outlinks[i][j] == 1:
					temp_hub += authority_scores[j]
			hub_scores[i] = temp_hub
			
		
		hub_sum = sum(hub_scores)
		
		for i in range(len(hub_scores)):
			hub_scores[i] /= hub_sum
	
	return authority_scores, hub_scores
					


pickle_file = input('Enter the name of the pickle file:\t')

if not os.path.isfile(pickle_file):
	n = int(input('Enter the size of the matrix:\t'))
	outlinks = []
	for i in range(n*n):
		temp = int(input('Enter the element:\t'))
		outlinks.append(temp)
	outlinks = np.reshape(outlinks, (n, n))
	pickle.dump(outlinks, open(pickle_file, 'wb'), protocol = 4)
else:
	print('Loading outlink matrix from %s' % (pickle_file))
	outlinks = pickle.load(open(pickle_file, 'rb'))

authority_scores, hub_scores = authority_hub_score(outlinks)
print("\nAuthority Scores:")
for i in (authority_scores):
	print(round(i, 4))
print("\nHub Scores:")
for i in (hub_scores):
	print(round(i, 4))
