#  else 子句在未出现异常时运行，循环的 else 子句在未出现 break 时运行

for n in range(2, 10):
	for x in range(2,n):
		if n % x == 0:
			print(n, "=", x,  "*", int(n/x))
			break;
		print("This is a test ", n, ":", x)
	else:
		print(n, " is a prime number")
print()



