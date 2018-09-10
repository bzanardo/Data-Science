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