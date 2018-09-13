import numpy as np
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from numpy import linalg as LA
import math


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

u0 = []
for i in range(0, 150):
	u0.append(1/math.sqrt(150))

U = []
U.append(u0)
V = []

for i in range (0, 1000):
	r = np.dot(A.T,U[i])
	v = normalize(r.reshape(-1, 1))
	V.append(v)
	k = np.dot(A,V[i])
	u = normalize(k.reshape(-1, 1))
	U.append(u)

print(U[0])
print(V[0])
