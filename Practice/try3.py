#

try:
	raise Exception("Spam", "Eggs")
except Exception as inst:
	print(type(inst))
	print(inst.args)
	print(inst)
	print(inst.args[0])
	print(inst.args[1])
	#print(inst.args[2])
print()

def this_fails():
	x = 1/0;
	
try:
	this_fails()
except ZeroDivisionError as ex:
	print("Handling run-time error:",  ex)
#except Exception as ex:
#	print(ex)

raise NameError("Nihao")





