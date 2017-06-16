
a, b = (0,1)
while b < 100:
	print(b,end=' '),   #// 用 ,end=' ' 可以禁止输出换行
	a,b = b, a + b
print()

a = 90
print("a = ", a),
