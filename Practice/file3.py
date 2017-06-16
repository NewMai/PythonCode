#

name = "1.txt"
with open(name, "r") as f:
	
	for line in f:
		print(line, end = '')
	
	print(f.closed)
	"""
	var = f.readline()
	while var:
		print(var, end = '')
		var = f.readline()
	"""
	print()
print(f.closed)



