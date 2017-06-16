#


class Mapping:
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)
	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)
	__update = update
	pass
	
class MappingSubClass(Mapping):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)
	pass

keys = ["A", "B", "C", "D"]
values = [1,2,3,4]
tmp = ["AAA", "BBB", "CCC"]
y = MappingSubClass(tmp)
y.update(keys,values)
print(y.items_list)
print()

#pbd.set_trace()

x = Mapping(tmp)
print(x.items_list)
print()





	
	