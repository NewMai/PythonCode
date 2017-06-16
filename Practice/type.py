#

class A:
	pass
	
x = A();
print(isinstance(x, A))

x = 123
print(isinstance(x, int))

x = "123asdf"
print(isinstance(x, str))

print(issubclass(bool, int))

print(issubclass(int, str))
x = u"123456sdgf"
print(type(x))

