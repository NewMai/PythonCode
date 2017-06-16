# u"" 表示 unicode 字符串

str1 = u"Hello word! "
print(str1)
print(str1 + u"123")

str2 = u"Hello\u0020word!"
print(str2)

str3 = u"Hello\\u0020word!"
print(str3)

print(str(str1))
print(len(str1))
print(len(str(str1)))

str3 = u"你好"
print(str(str3))
print(str3.encode('utf-8'))

str3 = u"我们"
print(str(str3))
tmp = str3.encode('utf-8')
print(tmp)
print(len(tmp))

str4 = unicode("\xc3\xa4\xc3\xb6\xc3\xbc", 'utf-8')
print(str4)

