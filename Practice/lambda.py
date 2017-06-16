#

def make_incrementor(n):
	''' 此处的 返回的其实是一个匿名的函数 '''
	return lambda x: x + n

	
f = make_incrementor(42)
print (f(20))
print (f(1))

pairs = [(1,'one'), (2, 'two'), (3, 'three'), (4,'four')]
pairs.append((5,'five'))
pairs.sort(key = lambda pair: pair[1])
print(pairs)

pp = sorted(pairs, key = lambda p: p[0], reverse = True)
for pair in pp:
	print(pair[1], pair[0])
