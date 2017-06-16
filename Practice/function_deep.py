

def ask_ok(promt, retries = 4, complaint = 'Yes or no, please!'):
	while True:
		ok = input(promt)
		if(ok in ('y', 'ye', 'yes')):
			return True
		if(ok in ('n', 'no', 'nop')):
			return False
		retries = retries - 1
		if(retries < 0):
			raise IOError('Refusenik user')
		print(complaint)

		
#ask_ok('Do you really want to quit?')		
#ask_ok('OK to overwrite the file?', 2)
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 3
def f(arg = i):
	print(arg)

i = 9
f()
f(i)
f()

def ff(a, L = []):
	L.append(a)
	return L

res = ff(1)
print(res)
res = ff(11)
print(res)
res = ff(111)
print(res)


def fff(a, L = None):
	if(L == None):
		L = []
	L.append(a)
	return L

res = fff(1)
print(res)
res = fff(11)
print(res)
res = fff(111)
print(res)


