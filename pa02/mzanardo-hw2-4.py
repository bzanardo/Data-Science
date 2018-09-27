import numpy as np
from scipy import stats
from sklearn import tree
import graphviz 


data = [[0 for x in range(4)] for y in range(150)] 
labels = []

with open("Dataset-film-data.csv") as f:
	next(f)
	counter = 0
	for line in f.readlines():
		i = 0
		for value in line.split(","):
			if i > 0:
				if i == 5:
					labels.append(value)
				else:
					data[counter][i - 1] = value

			i +=1

		counter += 1
f.close()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, labels)

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=["Ratings 1", "Ratings 2", "Ratings 3", "Ratings 4"]) 
graph = graphviz.Source(dot_data) 
graph.render(view=True)


