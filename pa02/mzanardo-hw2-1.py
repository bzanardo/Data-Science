import numpy as np
import math

def IG(data, indexedData, feature, givenClass):
	uncondEntropy = entropy(indexedData, givenClass)
	condEntropy = 0

	freq = {}
	totalSum = 0
	
	for k, v in indexedData.items():
		if indexedData[k][feature] in freq:
			freq[indexedData[k][feature]] += 1.0
			totalSum += 1
		else:
			freq[indexedData[k][feature]]  = 1.0
			totalSum += 1

	subset = {}

	for k, v in freq.items():
		prob = v / totalSum
		subset = {}
		for key, value in indexedData.items():
			if indexedData[key][feature] == k:
				subset[key] = value

		condEntropy += prob * entropy(subset, givenClass)

	ig = uncondEntropy - condEntropy

	return(ig)


def entropy(data, feature):
	freq = {}
	data_entropy = 0.0
	totalSum = 0

	for k, v in data.items():
		if data[k][feature] in freq:
			freq[data[k][feature]] += 1
			totalSum += 1
		else:
			freq[data[k][feature]]  = 1
			totalSum += 1

	for k, f in freq.items():
		ratio = f/totalSum
		if ratio != 1:
			data_entropy += (-ratio*math.log(ratio,2))
 
	return data_entropy


def checkResult(indexedData):
	wins = 0
	losses = 0
	for k, v in indexedData.items():
		for key, value in indexedData[k].items():
			if key == "Result":
				if value == "Win":
					wins += 1
				else:
					losses += 1
	if wins > losses:
		return("Win")
	else:
		return("Lose")


def ID3(data, indexedData, features, attribute = "Result"):

	if (len(features) == 0):
		result = checkResult(indexedData)
		return(result)

	else:

		infoGains = {}

		for f in features:			# Calculate information gain
			g = IG(data, indexedData, f, attribute)
			infoGains[g] = f

		largestGain = max(infoGains)

		if largestGain == 0:
			result = checkResult(indexedData)
			return(result)

		bestFeature = infoGains[largestGain]

		tree = {bestFeature : {}}

		updatedFeatures = []		# Update features
		for i in features:
			if i != bestFeature:
				updatedFeatures.append(i)

		subset = {"H/A" : [], "Top25" : [], "Media" : [], "Result" : []}
		for result in np.unique(data[bestFeature]):		# Split data
			subData = {}
			for k, v in indexedData.items():
				if indexedData[k][bestFeature] == result:
					subData[k] = {}
					for key, value in indexedData[k].items():
						if key == bestFeature:
							if indexedData[k][key] == result:
								subData[k] = v
								subset[key].append(value)


			subtree = ID3(data, subData, updatedFeatures, "Result")
			tree[bestFeature][result] = subtree


	
	return tree


def predict(tree, data):
	results = {}
	
	for key, value in data.items():
		prediction = False
		subtree = tree
		feature = list(tree.keys())[0]
		while prediction == False:
			result = data[key][feature]
			subtree = subtree[feature][result]
			if (subtree == 'Win') or (subtree == 'Lose'):
				results[key] = subtree
				prediction = True
				break
			else :
				feature = list(subtree.keys())[0]


	return results
			


# Load Training Data

count = 0
data = {"H/A" : [], "Top25" : [], "Media" : [], "Result" : []}
features = ["H/A", "Top25", "Media"]

f = open("Dataset-football-train.txt", "r")
for line in f:
	if count > 0:
		feature = 0
		for value in line.split():
			if feature == 3:
				if (value != "Home") and (value != "Away"):
					feature -= 1
				else:
					data["H/A"].append(value)	
			if feature == 4:
				data["Top25"].append(value)
			if feature == 5:
				data["Media"].append(value)
			if feature == 6:
				data["Result"].append(value)

			feature += 1
			
	count += 1


indexedData = {}

f = open("Dataset-football-train.txt", "r")
count = 0
for line in f:
	if count > 0:
		indexedData[count] = {}
		feature = 0
		for value in line.split():
			if feature == 3:
				if (value != "Home") and (value != "Away"):
					feature -= 1
				else:
					indexedData[count]["H/A"] = value	
			if feature == 4:
				indexedData[count]["Top25"] = value
			if feature == 5:
				indexedData[count]["Media"] = value
			if feature == 6:
				indexedData[count]["Result"] = value

			feature += 1
			
	count += 1

f.close()

tree = ID3(data, indexedData, features)
print(tree)


# Load Testing Data

count = 24
dataTest = {}

f = open("Dataset-football-test.txt", "r")
for line in f:
	if count > 24:
		dataTest[count] = {}
		feature = 0
		for value in line.split():
			if feature == 3:
				if (value != "Home") and (value != "Away"):
					feature -= 1
				else:
					dataTest[count]["H/A"] = value
			if feature == 4:
				dataTest[count]["Top25"] = value
			if feature == 5:
				dataTest[count]["Media"] = value
			if feature == 6:
				dataTest[count]["Result"] = value

			feature += 1
			
	count += 1

f.close()

r = predict(tree, dataTest)
print(r)




