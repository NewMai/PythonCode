#

def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	
	for arg in arguments:
		print(arg)
	print("-" * 40)
	
	# 按关键字进行排序
	keys = sorted(keywords.keys())
	for kw in keys : 
		print(kw, ":", keywords[kw])
	
	print()
	
	# 没有进行排序的结果
	keys = keywords.keys()
	for kw in keys : 
		print(kw, ":", keywords[kw])
	

cheeseshop("MaiLong", "It's very runny, sir.",
			"It's realy very, VERY runny, sir.",
			shopkeeper = "Michael, Plain",
			client = "John Cleese",
			sketch = "Cheese Shop Sketch" )
		
			
			
