#

def show_file(name):
	f = open("file.py", "r")
	var = f.readline()
	i = 1
	print("=" * 50)
	while var:
		#print(var, end = '')
		print(i, var, end = '')
		#print(i, repr(var))
		var = f.readline()
		i += 1
	print()
	print("=" * 50)
	print()
	f.close()	

var = "file.py"
show_file(var)




