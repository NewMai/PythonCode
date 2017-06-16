#

words = ['cat', 'window', 'defenestrate']

for w in words:
	print(w, ", len = ", len(w))
	if(len(w) < 5):
		print('这个字符串太短了')
	

for w in words[:]:
	print(w, ", len = ", len(w))
	if(len(w) > 5):
		words.insert(0, w + "插入的")
print(words)		


