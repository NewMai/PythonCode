#

import sys

for arg in sys.argv:
	print(arg)
print()

for arg in sys.argv[1:]:
	try:
		f = open(arg,"r")
	except IOError as e:
		print("Can not open file: ", arg)
		print("Exception : ", e)
	else:
		print(arg, " has ",  len(f.readlines()), "lines.")
		f.close()
