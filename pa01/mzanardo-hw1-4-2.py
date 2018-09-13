import numpy as np
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from numpy import linalg as LA

data = [[0 for x in range(5)] for y in range(150)]

with open("Dataset-film-data.csv") as f:
	next(f)
	for line in f.readlines():
		counter = 0
		for value in line.split(","):
			if counter == 0:
				k = int(value[1:])
			elif counter < 5:
				data[k - 1][counter - 1] = float(value)

			counter += 1

D = np.array(data)
A = normalize(D, axis=0)
U, S, V = svds(A, k = 3)
print(np.around(U, 2))
print(np.around(S, 2))
print(np.around(V, 2))