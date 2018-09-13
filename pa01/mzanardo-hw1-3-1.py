import numpy as np
from scipy import stats
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
r2 = []
r3 = []
r4 = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "r1":
			r1.append(float(value))
		if key == "r2":
			r2.append(float(value))
		if key == "r3":
			r3.append(float(value))
		if key == "r4":
			r4.append(float(value))


coefficients = {}

r1r2 = np.corrcoef(np.array(r1), np.array(r2))
coefficients["r1r2"] = r1r2

r1r3 = np.corrcoef(np.array(r1), np.array(r3))
coefficients["r1r3"] = r1r3

r1r4 = np.corrcoef(np.array(r1), np.array(r4))
coefficients["r1r4"] = r1r4

r2r3 = np.corrcoef(np.array(r2), np.array(r3))
coefficients["r2r3"] = r2r3

r2r4 = np.corrcoef(np.array(r2), np.array(r4))
coefficients["r2r4"] = r2r4

r3r4 = np.corrcoef(np.array(r3), np.array(r4))
coefficients["r3r4"] = r3r4

for k, v in coefficients.items():
	print(k + ": " + str(v))

