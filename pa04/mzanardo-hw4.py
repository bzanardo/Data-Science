
def getSupport(item, db):
	count = 0
	for k, v in db.items():
		if set(item).issubset(v):
			count += 1

	return count


transaction_db = {}

with open("Dataset-apriori.txt") as f:
	next(f)
	for line in f.readlines():
		k = int(line.split()[0])
		transaction_db[k] = []
		for value in line.split()[1:]:
			transaction_db[k].append(value)



			
		 
