#

class MyClass:
	"""A simple example class"""
	i = 123
	def f(self):
		return "Hello world"
	pass

	
#方法的特别之处在于实例对象作为函数的第一个参数传给了函数。
	
print(MyClass.i)
print(MyClass.f(1))   # 这个时候需要一个参数
print(MyClass.__doc__)
	
x = MyClass()
print(x)
print(x.__doc__)
print(x.i)
print(x.f())   # 这个时候就不需要参数了



