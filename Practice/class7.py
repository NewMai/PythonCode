#

class Test:
	#fun = "Test string"
	def fun(self):
		print("This is a test function")
	pass
	
x = Test()
y = x.fun
print(x.fun)
print(y())
print()

x.fun = "This is a attibute"

print(x.fun)
print(y())
print()

