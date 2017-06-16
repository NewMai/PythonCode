#

def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
	print("-- This parrot wouldn't", action)
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")
	print()
	
def write_multiple_items(file, seperator, *args):
	file.write(seperator.join(args))
	

a = list([1,2,3])
b = list(range(0,5))
print(a)	
print(b)
args = [3, 5]
c = list(range(*args))
print(c)

d = {"voltage":"four million", "state":"bleedin' demised", "action":"VOOM"}
parrot(**d)


