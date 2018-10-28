import numpy as np
from scipy.sparse.linalg import svds
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from numpy import linalg as LA

data = [[0 for x in range(5)] for y in range(150)]
genre = []

with open("Dataset-film-data.csv") as f:
	next(f)
	for line in f.readlines():
		counter = 0
		for value in line.split(","):
			if counter == 0:
				k = int(value[1:])
			elif counter < 5:
				data[k - 1][counter - 1] = float(value)
			else:
				genre.append(value)

			counter += 1

D = np.array(data)
A = normalize(D, axis=0)
U, S, V = svds(A, k = 2)
print(np.around(U, 2))
print(np.around(S, 2))
print(np.around(V, 2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

labels = {"ACTION\n" : {"color" : "red", "marker" : "o", "values" : {"x" : [], "y" : []}}, "COMEDY\n" : {"color" : "blue", "marker" : "v", "values" : {"x" : [], "y" : []}}, "ROMANCE\n" : {"color" : "green", "marker" : "s", "values" : {"x" : [], "y" : []}} }

for i in range(0, len(U)):
	labels[genre[i]]["values"]["x"].append(U[i][0])
	labels[genre[i]]["values"]["y"].append(U[i][1])


for k, v in labels.items():
	l = k
	for i in range(len(labels[k]["values"]["x"])):
		ax.scatter(labels[k]["values"]["x"][i], labels[k]["values"]["y"][i], c=labels[k]["color"], label=l, marker=labels[k]["marker"])
		l = "_nolegend_"

plt.title('First 2 Left-Singular Vectors')
plt.xlabel("Singular Vector 1")
plt.ylabel("Singular Vector 2")
plt.legend(loc=2)
plt.show()