str = "py" "thon"
str2 = " is easy\n"
print(str)
print((str + str2) * 3)

text = ('this is a ' 
	'test')
print(text)
print(text[2])

print(text[-3])  # 复数的索引将会导致字符串从右边开始计算

print(text[0:8])  # 获取子串  ，  切片

print(text[0:])
print(text[:8])
print(text[-5:])  # 从倒数第五个开始

print(text[42:]) # 当上边界比下边界大时(即切片左值大于右值)就返回空字符串
print(text[:42]) #一个过大的索引值(即下标值大于字符串实际长度)将被字符串实际长度所代替

# Python字符串不可以被更改 — 它们是 不可变 的

print("Python字符串不可以被更改 — 它们是 不可变 的\n")

s1 = 'J' + text[1:]
print(s1)
print(len(s1))





