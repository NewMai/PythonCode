

def file_op(name):
	f = open(name, "r")
	var = f.readlines()
	to = open("222.txt", "w")
	i = 1
	for line in var:
		#print(i, line, end = "")
		tmp = "{0} {1}".format(i, line)
		to.write(tmp)
		print(to.tell())
		i += 1
	print()
	f.close()
	to.close()
	
var = "file2.py"
file_op(var)



