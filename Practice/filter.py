#

def f(x) : 
	return x % 3 == 0 or x % 5 == 0

l = list(filter(f, range(2,50)))
print(l)

def cube(x):
	return x * x * x
	
m = list(map(cube, range(1, 11)))
print(m)


def add(x, y): return x + y
seq = range(8)
r = list(map(add, seq, seq))
print(r)



#rr = reduce(add, range(1,11))
#print(rr)

def calcAdd(a, b):
	if(a > b): a,b = b,a
	res = range(a,b)
	for x in res:
		pass

print(sum(range(1, 101)))
