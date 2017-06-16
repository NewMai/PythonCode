#

def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
	print("-- This parrot would't", action)
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")
	print()
	
parrot(1000)	
parrot(voltage = 1000)	
parrot(voltage = 1000,action = "VOOOOOM")
parrot(action = "VOOOOOM", voltage = 100000)
parrot('a million', 'breft of life', 'jump')
parrot("a thousand", state = "pushing up the daisies")

parrot(100, voltage = 5.5)


