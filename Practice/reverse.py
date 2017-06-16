#

a = "This is just a test!"

def MyReverse(s):

	L = s
	L = L.split(" ")	
	#L.reverse()  # 方法一
	L = L[::-1]   # 方法二
	L = ' '.join(L)
	return L
	
var = MyReverse(a)
print(var)
print(*var)