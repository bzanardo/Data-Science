import numpy as np

def IG(data, indexedData, feature, givenClass):
	uncondEntropy = entropy(indexedData, givenClass)
	condEntropy = 0

	#values,count = np.unique(data[feature],return_counts=True)
	#totalSum = np.sum(count)
	freq = {}
	totalSum = 0
	
	for k, v in indexedData.items():
		if data[k][feature] in values:
			freq[data[k][feature]] += 1.0
			totalSum += 1
		else:
			freq[data[k][feature]]  = 1.0
			totalSum += 1

	subset = {}

	for k, v in freq:
		prob = v / totalSum
		for key, value in indexedData.items():
			if indexedData[key][feature] == k:
				subset[key] = value

		condEntropy += prob * entropy(subset, givenClass)

	ig = uncondEntropy - condEntropy

	return(ig)


def entropy(data, feature):
	freq = {}
	data_entropy = 0.0

	for k, v in data.items():
		if data[k][feature] in freq:
			freq[data[k][feature]] += 1.0
		else:
			freq[data[k][feature]]  = 1.0
 
	for k, f in freq.items():
		data_entropy += (-f/len(data)) * np.log2(f/len(data)) 
 
	return data_entropy


def ID3(data, indexedData, features, attribute = "Result", parentNode = None):

	if (len(features) == 0):
		return parentNode

	infoGains = {}

	for f in features:			# Calculate information gain
		g = IG(data, indexedData, f, attribute)
		infoGains[g] = f

	largestGain = max(infoGains)
	if largestGain < 0:
		return parentNode

	bestFeature = infoGains[largestGain]

	parentNode = bestFeature
	tree = {bestFeature : {}}

	updatedFeatures = []		# Update features
	for i in features:
		if i != bestFeature:
			updatedFeatures.append(i)

	splitData = []
	for result in np.unique(data[bestFeature]):		# Split data
		subData = {}
		for k, v in indexedData.items():
			if indexedData[k][bestFeature] == result:
				subData[k] = {}
				for key, value in indexedData[k].items():
					if key != bestFeature:
						subData[k][key] = value

		splitData.append(subData)

		subtree = ID3(subData, subData, features, "Result", parentNode)
		tree[bestFeature] = subtree

		return tree

	    

# Training Data

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


ID3(data, indexedData, features)


