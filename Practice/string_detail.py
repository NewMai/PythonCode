#

s = 123 + 456
print (s)
var = str(s)
print (var)
print()

x = 10*3.25
y = 200 * 21
var = repr(x + 10) + " " + repr(y)
print(var)
print()


hello = 'How are you'
print(hello)
var = repr(hello)
print(var)
print()


hello = 'hello world\n'
print(hello)
var = repr(hello)
print(var)
print()


L = [1,32,5,6,58,"ger", "ehgtjhryj", ('a', 1)]
print(L)
var = repr(L)
print(var)
print()

L = {"a": 1, "b":2}
print(L)
var = repr(L)
print(var)
print()


for x in range(1, 60):
	print(
	repr(x).ljust(5), 
	repr(x**2).rjust(8), 
	repr(x**3).ljust(12)
	)
print()	

var = "{0:02d} {1:03d} {2:04d}"
for x in range(1, 21):
	print(var.format(x, x**2, x**3))
print()	



x = '-3.14'
var = x.zfill(10)
print(var)
print()	


x = 'This is just a {}, {}'
var = x. format("test", "are you ready?")
print(var)
print()	

x = 'This is just a {A}, {B}'
var = x. format(A = "test", B = "are you ready?")
print(var)
print()	


import math
x = 3.14
var = "This is PI : {0:.10f}".format(x)
print(var)
var = "This is PI : {0:3f}".format(math.pi)
print(var)
var = "This is PI : %f"%(math.pi) # 传统方式
print(var)
print()	

