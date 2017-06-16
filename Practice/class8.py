

def f1(self, x, y):
	return min(x,y)
def f2(self, x):
	return x+10

	
class C:
	f = f1
	def g(self):
		return repr(self) + "Hello world"
	h = g
	
print(f1(0,1,2))
x = C();
print(x.f(4,5))
print(x.g())
print(x.h())
x.h = f2
print(x.h(0, 6))



	
	