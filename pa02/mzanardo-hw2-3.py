
# Training Data

count = 0
data = {}

f = open("Dataset-football-train.txt", "r")
for line in f:
	if count > 0:
		data[count] = {}
		feature = 0
		for value in line.split():
			if feature == 1:
				data[count]["Date"] = value
			if feature == 2:
				data[count]["Opponent"] = value
			if feature == 3:
				if (value != "Home") and (value != "Away"):
					data[count]["Opponent"] + value
					feature -= 1
				else:
					data[count]["H/A"] = value	
			if feature == 4:
				data[count]["Top25"] = value
			if feature == 5:
				data[count]["Media"] = value
			if feature == 6:
				data[count]["Result"] = value

			feature += 1
			
	count += 1

f.close()

resultCount = {"Win" : 0, "Lose" : 0, "P(W)" : 0, "P(L)" : 0}
for k, v in data.items():
	if data[k]["Result"] == "Win":
		resultCount["Win"] += 1
	else:
		resultCount["Lose"] += 1

resultCount["P(W)"] = resultCount["Win"] / 24
resultCount["P(L)"] = resultCount["Lose"] / 24


probHA = {"Home": {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0}, "Away" : {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0}}

for k, v in data.items():
	for key, value in data[k].items():
		if key == "H/A":
			if data[k][key] == "Home":
				probHA["Home"]["total"] += 1
				if data[k]["Result"] == "Win":
					probHA["Home"]["Win"] += 1
				else:
					probHA["Home"]["Lose"] += 1
			else:
				probHA["Away"]["total"] += 1
				if data[k]["Result"] == "Win":
					probHA["Away"]["Win"] += 1
				else:
					probHA["Away"]["Lose"] += 1

probWin = probHA["Home"]["Win"] / resultCount["Win"]
probLose = probHA["Home"]["Lose"] / resultCount["Lose"]
probHA["Home"]["P(W)"] = probWin
probHA["Home"]["P(L)"] = probLose

probWin = probHA["Away"]["Win"] / resultCount["Win"]
probLose = probHA["Away"]["Lose"] / resultCount["Lose"]
probHA["Away"]["P(W)"] = probWin
probHA["Away"]["P(L)"] = probLose

probTop25 = {"In": {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0}, "Out" : {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0}}

for k, v in data.items():
	for key, value in data[k].items():
		if key == "Top25":
			if data[k][key] == "In":
				probTop25["In"]["total"] += 1
				if data[k]["Result"] == "Win":
					probTop25["In"]["Win"] += 1
				else:
					probTop25["In"]["Lose"] += 1
			else:
				probTop25["Out"]["total"] += 1
				if data[k]["Result"] == "Win":
					probTop25["Out"]["Win"] += 1
				else:
					probTop25["Out"]["Lose"] += 1

probWin = probTop25["In"]["Win"] / resultCount["Win"]
probLose = probTop25["In"]["Lose"] / resultCount["Lose"]
probTop25["In"]["P(W)"] = probWin
probTop25["In"]["P(L)"] = probLose

probWin = probTop25["Out"]["Win"] / resultCount["Win"]
probLose = probTop25["Out"]["Lose"] / resultCount["Lose"]
probTop25["Out"]["P(W)"] = probWin
probTop25["Out"]["P(L)"] = probLose

probMedia = {"NBC": {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0}, 
			 "ABC" : {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0},
			 "FOX" : {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0},
			 "ESPN" : {"Win" : 0, "Lose" : 0, "total" : 0, "P(W)" : 0, "P(L)" : 0}}

for k, v in data.items():
	for key, value in data[k].items():
		if key == "Media":
			if data[k][key] == "NBC":
				probMedia["NBC"]["total"] += 1
				if data[k]["Result"] == "Win":
					probMedia["NBC"]["Win"] += 1
				else:
					probMedia["NBC"]["Lose"] += 1
			elif data[k][key] == "ABC":
				probMedia["ABC"]["total"] += 1
				if data[k]["Result"] == "Win":
					probMedia["ABC"]["Win"] += 1
				else:
					probMedia["ABC"]["Lose"] += 1
			elif data[k][key] == "FOX":
				probMedia["FOX"]["total"] += 1
				if data[k]["Result"] == "Win":
					probMedia["FOX"]["Win"] += 1
				else:
					probMedia["FOX"]["Lose"] += 1
			elif data[k][key] == "ESPN":
				probMedia["ESPN"]["total"] += 1
				if data[k]["Result"] == "Win":
					probMedia["ESPN"]["Win"] += 1
				else:
					probMedia["ESPN"]["Lose"] += 1

probWin = probMedia["NBC"]["Win"] / resultCount["Win"]
probLose = probMedia["NBC"]["Lose"] / resultCount["Lose"]
probMedia["NBC"]["P(W)"] = probWin
probMedia["NBC"]["P(L)"] = probLose

probWin = probMedia["ABC"]["Win"] / resultCount["Win"]
probLose = probMedia["ABC"]["Lose"] / resultCount["Lose"]
probMedia["ABC"]["P(W)"] = probWin
probMedia["ABC"]["P(L)"] = probLose

probWin = probMedia["FOX"]["Win"] / resultCount["Win"]
probLose = probMedia["FOX"]["Lose"] / resultCount["Lose"]
probMedia["FOX"]["P(W)"] = probWin
probMedia["FOX"]["P(L)"] = probLose

probWin = probMedia["ESPN"]["Win"] / resultCount["Win"]
probLose = probMedia["ESPN"]["Lose"] / resultCount["Lose"]
probMedia["ESPN"]["P(W)"] = probWin
probMedia["ESPN"]["P(L)"] = probLose

# Test Data

count = 24
dataTest = {}

f = open("Dataset-football-test.txt", "r")
for line in f:
	if count > 24:
		dataTest[count] = {}
		feature = 0
		for value in line.split():
			if feature == 1:
				dataTest[count]["Date"] = value
			if feature == 2:
				dataTest[count]["Opponent"] = value
			if feature == 3:
				if (value != "Home") and (value != "Away"):
					dataTest[count]["Opponent"] + value
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


for k,v in dataTest.items():
	featureHA = dataTest[k]["H/A"]
	featureTop25 = dataTest[k]["Top25"]
	featureMedia = dataTest[k]["Media"]

	# Prob Win

	winHA = probHA[featureHA]["P(W)"]
	winTop25 = probTop25[featureTop25]["P(W)"]
	winMedia = probMedia[featureMedia]["P(W)"]
	probWin = resultCount["P(W)"]

	finalProbWin = winHA * winTop25 * winMedia * probWin

	# Prob Lose

	loseHA = probHA[featureHA]["P(L)"]
	loseTop25 = probTop25[featureTop25]["P(L)"]
	loseMedia = probMedia[featureMedia]["P(L)"]
	probLose = resultCount["P(L)"]

	finalProbLose = loseHA * loseTop25 * loseMedia * probLose

	if finalProbWin > finalProbLose:
		print(str(k) + ": " + dataTest[k]["Opponent"] + ", Predicted: Win, Actual: " + dataTest[k]["Result"])
	else:
		print(str(k) + ": " + dataTest[k]["Opponent"] + ", Predicted: Lose, Actual: " + dataTest[k]["Result"])




