
try:
	raise KeyboardInterrupt
except KeyboardInterrupt as e:
	print("Exception: ", e)
finally:
	print("Good bye")
print()
	
def divive(x, y):
	try:
		result = x / y
		print("{0}/{1} = {2}".format(x, y, result))
	except ZeroDivisionError as er:
		print("Error: ", er)
	finally:
		print("Completed!")
	print()		
	
		
divive(1,2)
divive(2,0)
divive('d','f')
	
	
	