#

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print(fruit)

def judge(a, b):
	if( a in b):
		print(a, "in", b)
	else:
		print(a, "not in", b)
	

judge('orange', fruit)
judge("applee", fruit)

a = set('abcd')
b = set('cdef')

# 集合的简单操作
print(a)
print(b)
print(a-b)
print(a | b)
print(a & b)
print(a ^ b)


c = {x for x in 'gdafgrdgdsdgregsefsff' if x not in 'grdsca'}
print(c)
