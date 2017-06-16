# 


def fib(n):
	"""这个函数打印斐波那契数列"""
	a,b = 0,1
	while(a < n):
		print(a, end = ' ')
		a,b = b, a+ b
	print()

def fib2(n):
	"""这个函数返回斐波那契数列"""
	result = []
	a,b = 0,1
	while(a < n):
		result.append(a)
		a,b = b, a+ b
	return result
	
fib(100)
fib(1000)
res1 = fib2(100)
print(res1)
	
	