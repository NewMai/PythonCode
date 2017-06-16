#

class MyClass:
	def __init__(self):
		pass
	def __init__(self, x, y):
		self.data = [1,2,3]		
		self.x = x
		self.y = y
	pass

	
x = MyClass(1,2)
print(x)	
print(x.data)
print(x.x)
print(x.y)
x.count = 10
print(x.count)
#print(count)
print()

"""
y = MyClass()
print(x)	
print(x.data)
print(x.x)
print(x.y)
"""


