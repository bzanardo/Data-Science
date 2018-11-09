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
		#print(k)
		print(k[:index])
		print(current_item[:index])

		if k == current_item:
	 		continue

		if k[:index] == current_item[:index]:
			new_item = current_item + k[-1]
			candidates[new_item] = list(it.combinations(list(new_item), lenght))#[current_item, k, current_item[1]+ k[1]]
		else:
			current_item = k

	return(candidates)


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

#candidates = {}
#current_item = list(two_itemset.keys())[0]

print(two_itemset)
candidates = findCandidates(two_itemset, 3)
print(candidates)

# for k, v in two_itemset.items():
# 	if k == current_item:
# 		continue
# 	if k[0] == current_item[0]:
# 		new_item = current_item + k[1:]
# 		candidates[new_item] = [current_item, k, current_item[1]+ k[1]]
# 	else:
# 		current_item = k


# for k, v in candidates.items():
# 	valid = True
# 	for i in v:
# 		if i not in two_itemset:
# 			valid = False
# 			break 
# 		else:
# 			sup = two_itemset[str(i)]

# 		if sup < min_sup:
# 			valid = False
# 			break

# 	if valid:
# 		supp = getSupport(list(k), transaction_db)
# 		if supp >= min_sup:
# 			three_itemset[k] = supp









			
		 
