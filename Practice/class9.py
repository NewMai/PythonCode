

g_data = ["x", "y", "z"]

class Bag:
	def __init__(self):
		self.data = g_data
	def add(self, x):
		self.data.append(x)
	def addTwice(self,x):
		self.add(x)
		self.add(x)

		
x = Bag()
print(x)
print(x.data)
print()

for i in range(1, 10):
	x.add(i)
print(x.data)
print()

for i in range(11, 20):
	x.addTwice(i)
print(x.data)
print()

del(g_data[0: 5])
print(x.data)
print()

g_data.insert(5, "Test")
print(x.data)
print()


k = "This is a string"
print(type(k))
print(dir(k))
print()

res = 123
print(type(res))
print(dir(res))
print()

