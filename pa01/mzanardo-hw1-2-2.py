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

r3 = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "r3":
			r3.append(value)


plt.figure()
plt.hist(np.array(r3).astype(np.float), 10)
plt.title('Avg. Rating Website 3')
plt.show()
