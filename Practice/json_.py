#

import json
import sys
L = [1, 'sample', 'list']
var = json.dumps(L)
print (var) 

name = "1.txt"
f = open(name, "w")
L = {"A": 1, "B": 2, 'C': 3}
var = json.dump(L, f)
print (var) 
f.close()

f = open(name, "r")
var = json.load(f)
print(var)
f.close()

for x in var.items():
	print(x[0], x[1])


