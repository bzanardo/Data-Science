import numpy as np
from scipy import stats

data = {}

with open("Dataset-film-data.csv") as f:
	next(f)
	for line in f.readlines():
		counter = 0
		for value in line.split(","):
			if counter == 0:
				k = value
				data[value] = {}
			elif counter < 5:
				data[k]["r" + str(counter)] = value
			else:
				data[k]["genre"] = value

			counter += 1
r1 = []
r2 = []
r3 = []
r4 = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "r1":
			r1.append(value)
		if key == "r2":
			r2.append(value)
		if key == "r3":
			r3.append(value)
		if key == "r4":
			r4.append(value)


r1 = stats.zscore(np.array(r1).astype(np.float))
print("Max r1: ", max(r1))
print("Min r1: ", min(r1))

r2 = stats.zscore(np.array(r2).astype(np.float))
print("Max r2: ", max(r2))
print("Min r2: ", min(r2))

r3 = stats.zscore(np.array(r3).astype(np.float))
print("Max r3: ", max(r3))
print("Min r3: ", min(r3))

r4 = stats.zscore(np.array(r4).astype(np.float))
print("Max r4: ", max(r4))
print("Min r4: ", min(r4))
