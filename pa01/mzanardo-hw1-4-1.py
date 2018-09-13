import numpy as np
from scipy import stats
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
C = np.dot(A.T, A)
eigenValues,eigenVectors = LA.eigh(C)

eigenValues = eigenValues[:k]
eigenVectors = eigenVectors[:,:k]

print(np.around(eigenValues,2))
print(np.around(eigenVectors,2))