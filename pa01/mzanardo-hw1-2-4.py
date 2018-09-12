import numpy as np
import matplotlib.pyplot as plt
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

genre = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "genre":
			genre.append(value)

g = {}

for i in genre:
	g[i] = {"r1" : [], "r3" : [], "color" : "", "marker" : ""}
	if i == "ACTION\n":
		g[i]["color"] = "red"
		g[i]["marker"] = "o"
	if i == "COMEDY\n":
		g[i]["color"] = "blue"
		g[i]["marker"] = "v"
	if i == "ROMANCE\n":
		g[i]["color"] = "green"
		g[i]["marker"] = "s"

for k, v in data.items():
	genre = data[k]["genre"]
	g[genre]["r1"].append(float(data[k]["r1"]))
	g[genre]["r3"].append(float(data[k]["r3"]))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for k,v in g.items():
	ax.scatter(g[k]["r1"], g[k]["r3"], c= g[k]["color"], label=k, marker=g[k]["marker"])

plt.title('Avg. Rating Website 1 x Avg. Rating Website 3')
plt.xlabel("avg. rating website 1")
plt.ylabel("avg. rating website 3")
plt.legend(loc=2)
plt.show()
