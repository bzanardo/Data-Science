
import statistics as stats
import math
import matplotlib.pyplot as plt

def euclidean(x1, y1, x2, y2):
	x = (x1 - x2) ** 2
	y = (y1 - y2) ** 2
	dist = math.sqrt(x + y)
	
	return dist


data = {}
#k = ""

with open("Dataset-clustering.txt") as f:
	next(f)
	for line in f.readlines():
		counter = 0
		k = ""
		for value in line.split():
			if (value.isdigit() == False):
				k += value
				counter = 0
			elif (value.isdigit() == True) and (counter == 1):
				data[k] = {}

			if counter == 1:
				data[k]["wins15"] = value
			elif counter == 2:
				data[k]["wins17"] = value
			elif counter == 3:
				data[k]["rank15"] = value
			elif counter == 4:
				data[k]["rank17"] = value


			counter += 1

wins15 = []
wins17 = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "wins15":
			wins15.append(float(value))
		if key == "wins17":
			wins17.append(float(value))

cent1X = 7
cent1Y = 7
cent2X = 14
cent2Y = 14

cluster1X = []
cluster1Y = []
cluster2X = []
cluster2Y = []

clusters = [0] * 12
changed = True


while (changed == True):

	changed = False

	for i in range(len(wins15)):
		dist1 = euclidean(wins15[i], wins17[i], cent1X, cent1Y)
		dist2 = euclidean(wins15[i], wins17[i], cent2X, cent2Y)

		if clusters[i] == 0:
			changed = True

		if (dist1 < dist2):
			cluster1X.append(wins15[i])
			cluster1Y.append(wins17[i])
			if (clusters[i] != 1):
				changed = True

			clusters[i] = 1

		else:
			cluster2X.append(wins15[i])
			cluster2Y.append(wins17[i])
			if (clusters[i] != 2):
				changed = True

			clusters[i] = 2


	if changed == False:
		break;

	cent1X = stats.mean(cluster1X)
	cent1Y = stats.mean(cluster1Y)

	cent2X = stats.mean(cluster2X)
	cent2Y = stats.mean(cluster2Y)
	
	cluster1X = []
	cluster1Y = []
	cluster2X = []
	cluster2Y = []


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for i in range(len(cluster1X)):
	ax.scatter(cluster1X[i], cluster1Y[i], c="r")

for i in range(len(cluster2X)):
	ax.scatter(cluster2X[i], cluster2Y[i], c="b")


ax.scatter(cent1X, cent1Y, c="r", marker="x", label="Centroid Cluster 1")
ax.scatter(cent2X, cent2Y, c="b", marker="x", label="Centroid Cluster 2")

plt.xlabel("Wins in 2015")
plt.ylabel("Wins in 2017")
plt.title("K-Means Clustering Centroids #1")
plt.legend(loc=5)
plt.show()

cent1X = 7
cent1Y = 7
cent2X = 7
cent2Y = 14

cluster1X = []
cluster1Y = []
cluster2X = []
cluster2Y = []

clusters = [0] * 12
changed = True


while (changed == True):

	changed = False

	for i in range(len(wins15)):
		dist1 = euclidean(wins15[i], wins17[i], cent1X, cent1Y)
		dist2 = euclidean(wins15[i], wins17[i], cent2X, cent2Y)

		if clusters[i] == 0:
			changed = True

		if (dist1 < dist2):
			cluster1X.append(wins15[i])
			cluster1Y.append(wins17[i])
			if (clusters[i] != 1):
				changed = True

			clusters[i] = 1

		else:
			cluster2X.append(wins15[i])
			cluster2Y.append(wins17[i])
			if (clusters[i] != 2):
				changed = True

			clusters[i] = 2


	if changed == False:
		break;

	cent1X = stats.mean(cluster1X)
	cent1Y = stats.mean(cluster1Y)

	cent2X = stats.mean(cluster2X)
	cent2Y = stats.mean(cluster2Y)
	
	cluster1X = []
	cluster1Y = []
	cluster2X = []
	cluster2Y = []


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for i in range(len(cluster1X)):
	ax.scatter(cluster1X[i], cluster1Y[i], c="r")

for i in range(len(cluster2X)):
	ax.scatter(cluster2X[i], cluster2Y[i], c="b")


ax.scatter(cent1X, cent1Y, c="r", marker="x", label="Centroid Cluster 1")
ax.scatter(cent2X, cent2Y, c="b", marker="x", label="Centroid Cluster 2")

plt.xlabel("Wins in 2015")
plt.ylabel("Wins in 2017")
plt.title("K-Means Clustering Centroids #2")
plt.legend(loc=5)
plt.show()


