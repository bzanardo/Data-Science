import numpy as np
import pylab
import scipy.stats as stats
import statsmodels.graphics.gofplots as sm
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
r3 = []

for k, v in data.items():
	for key, value in data[k].items():
		if key == "r1":
			r1.append(float(value))
		if key == "r3":
			r3.append(float(value))


x = sm.ProbPlot(np.array(r1))
y = sm.ProbPlot(np.array(r3))
fig = sm.qqplot_2samples(x, y, xlabel="avg rating website 1 quantiles", ylabel="avg rating website 3 quantiles", line="r")
plt.title("Q-Q Plot")
plt.show()
