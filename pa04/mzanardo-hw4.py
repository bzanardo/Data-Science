import itertools as it


def getSupport(item, db):
	count = 0
	for k, v in db.items():
		if set(item).issubset(v):
			count += 1

	return count

def findCandidates(db, lenght):
	index = lenght - 2
	candidates = {}
	keys = list(db.keys())
	current_item = keys[0]
	count = 0


	for k, v in db.items():
		i = keys.index(k) + 1
		for j in range(i, len(keys)):
			current_item = keys[j]

			if k == current_item:
	 			continue

			if k[:index] == current_item[:index]:
				new_item = k + current_item[-1]
				candidates[new_item] = [''.join(x) for x in it.combinations(new_item, lenght - 1)]
			else:
				continue

	return(candidates)

def prunning(candidates, db, transaction_db):
	valid_itemset = {}
	for k, v in candidates.items():
		valid = True
		for i in v:
			if i not in db:
				valid = False
				break 
			else:
				sup = db[str(i)]

			if sup < min_sup:
				valid = False
				break

		if valid:
			sup = getSupport(list(k), transaction_db)
			if sup >= min_sup:
				valid_itemset[k] = sup

	return(valid_itemset)



transaction_db = {}
with open("Dataset-apriori.txt") as f:
	next(f)
	for line in f.readlines():
		k = int(line.split()[0])
		transaction_db[k] = []
		for value in line.split()[1:]:
			transaction_db[k].append(value)

one_itemset = {}
two_itemset = {}
three_itemset = {}
four_itemset = {}

min_sup = 2
items = ['a', 'b', 'c', 'd', 'e']

for i in items:
	sup = getSupport([i], transaction_db)
	if sup >= min_sup:
		one_itemset[i] = sup

two_comb = list(it.combinations(one_itemset.keys(), 2))

for i in two_comb:
	sup = getSupport(list(i), transaction_db)
	if sup >= min_sup:
		key = str(i[0]) + str(i[1])
		two_itemset[key] = sup

candidates = findCandidates(two_itemset, 3)
three_itemset = prunning(candidates, two_itemset, transaction_db)

candidates = findCandidates(three_itemset, 4)
four_itemset = prunning(candidates, three_itemset, transaction_db)

print("frequent 1-itemsets")
for k, v in one_itemset.items():
	print(k + ": " + str(v))

print("frequent 2-itemsets")
for k, v in two_itemset.items():
	print(k + ": " + str(v))

print("frequent 3-itemsets")
for k, v in three_itemset.items():
	print(k + ": " + str(v))












			
		 
