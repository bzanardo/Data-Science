import itertools as it


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

print(two_itemset)





			
		 
