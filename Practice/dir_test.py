#

import function_test
import sys

def print_dir(var):
	for x in var:
		print(x)
	print()
	
def print_attrib(var):
	print("__builtins__ ", var.__builtins__)
	print("__cached__ ", var.__cached__)
	print("__doc__ ", var.__doc__)
	print("__file__ ", var.__file__)
	print("__loader__ ", var.__loader__)
	print("__name__ ", var.__name__)
	print("__package__ ", var.__package__)
	print("__spec__ ", var.__spec__)
	print()

var = dir()
print_dir(var)
print()

var = dir(function_test)
print_dir(var)
print()

print_attrib(function_test)
print()

var = dir(sys)
print_dir(var)
print()

print(sys.__doc__)
print(sys.__stdin__)
print()






