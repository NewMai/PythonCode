#

L = ["aaa", "bbb", "ccc"]
for i,v in enumerate(L):
	print(i,v)
	if v == "bbb":
		L[i] = "BBB"

print(L)


# 同时循环两个或更多的序列，可以使用 zip() 整体打包:


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
str = "What's your {0}? It is {1}";
for q,a in zip(questions, answers):
	print(str.format(q,a))
print()

print('Reversed:')	
for q,a in zip(reversed(questions), reversed(answers)):
	print(str.format(q,a))

print()
basket = ["apple", "orange", "pear", "apple", "orange", "banana"]
for f in sorted(set(basket)):
	print(f)
print()


T =  (123,456,212,454,5,12,45,454,54)
for i,v in enumerate(T):
	print(i,v)
print()	

knights = {"aaa": "The first", "bbb": "The second", "ccc":"The third"}
# for k,v in knights.iteritems():  # 这是老版本的方法
for k,v in knights.items():
	print(k,v)
print()	

words = ['cat', 'window', 'defenestrate', '123']	
for w in words[:]:
	if len(w) < 6:
		words.insert(0,"Test " + w)
	print(w)
print(words)	

