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
			
genre = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "genre":
			genre.append(value)

g = {}

for i in genre:
	g[i] = []

for k, v in data.items():
	genre = data[k]["genre"]
	g[genre].append(float(data[k]["r1"]))

x = []
y = []

for k, v in g.items():
	x.append(k)
	avg = sum(g[k]) / len(g[k])
	y.append(avg)

plt.figure()
plt.bar(x, y)
plt.title('Avg. Rating Website 1')
plt.show()
