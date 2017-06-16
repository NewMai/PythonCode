#

while True:
	try:
		x = input("Please input x:")
		x = int(x)
		y = input("Please input y:")
		y = int(y)
		print(x / y)
		break
	except ValueError:
		print("Oops! Try again...")
	except ZeroDivisionError:
		print("Oops! ZeroDivisionError...")
	except (RuntimeError, TypeError, NameError):
		pass
	print()
print("Today is a great day!")



