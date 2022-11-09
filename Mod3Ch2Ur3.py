d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
d1 = {}
for keys,value in d.items():
	d1[value] = keys
print(d1)