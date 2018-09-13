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


r1 = []
r3 = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "r1":
			r1.append(value)
		if key == "r3":
			r3.append(value)

d = np.linspace(0, 10, 21)
r1Count = {}
r3Count = {}

for i in d:
	r1Count[i] = 0
	r3Count[i] = 0

for i in d:
	for j in r1:
		if float(j) >= float(i):
			if float(j) < (float(i) + float(0.5)):
				r1Count[i] += 1

	for k in r3:
		if float(k) >= float(i):
			if float(k) < (float(i) + float(0.5)):
				r3Count[i] += 1

r1Freq = []
for k, v in r1Count.items():
	freq = r1Count[k] / 150
	if freq == 0:
		freq = 0.00000001

	r1Freq.append(freq)

r3Freq = []
for k, v in r3Count.items():
	freq = r3Count[k] / 150
	if freq == 0:
		freq = 0.00000001

	r3Freq.append(freq)

print(stats.entropy(r1Freq, r3Freq))


