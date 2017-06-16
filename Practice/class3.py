

class MyClass:
	def f(self):
		return "Hello world"

	pass


x = MyClass()
#print(MyClass)
#print(x)

y = x.f;   # 这是一个方法对象
print(y())



