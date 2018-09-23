import numpy as np
from scipy import stats
from sklearn import tree
import graphviz 


data = [[0 for x in range(5)] for y in range(150)] 

with open("Dataset-film-data.csv") as f:
	next(f)
	counter = 0
	for line in f.readlines():
		i = 0
		for value in line.split(","):
			if i > 0:
				if i == 5:
					if value == "ACTION\n":
						v = 0
					if value == "COMEDY\n":
						v = 1
					if value == "ROMANCE\n":
						v = 2
				else:
					v = value
							
				data[counter][i - 1] = v

			i +=1

		counter += 1
f.close()

labels = []

for j in range(0, 150):
	labels.append(j)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, labels)

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=["Ratings 1", "Ratings 2", "Ratings 3", "Ratings 4", "Genre"]) 
graph = graphviz.Source(dot_data) 
graph.render(view=True)


