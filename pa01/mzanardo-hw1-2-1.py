import numpy as np
import matplotlib.pyplot as plt

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

for k, v in data.items():
	for key, value in data[k].items():
		if key == "r1":
			r1.append(value)

plt.figure()
plt.boxplot(np.array(r1).astype(np.float))
plt.title('Avg. Rating Website 1')
plt.show()