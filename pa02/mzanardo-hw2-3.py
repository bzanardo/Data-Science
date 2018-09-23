

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

probWin = probHA["Home"]["Win"] / probHA["Home"]["total"]
probLose = probHA["Home"]["Lose"] / probHA["Home"]["total"]
probHA["Home"]["P(W)"] = probWin
probHA["Home"]["P(L)"] = probLose

probWin = probHA["Away"]["Win"] / probHA["Away"]["total"]
probLose = probHA["Away"]["Lose"] / probHA["Away"]["total"]
probHA["Away"]["P(W)"] = probWin
probHA["Away"]["P(L)"] = probLose

print(probHA)



