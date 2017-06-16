


d = {'e':10, 'a':11, 'c':9, 'd':41, 'b':2,}
print(d)

dd = sorted(d.items(), key = lambda x: x[0])
print(dd)

dd = sorted(d.items(), key = lambda x: x[1])
print(dd)

dd = sorted(d.items(), key = lambda x: x[1], reverse = True)
print(dd)
print()





t = ('dfe', 'dgdfg', 'wegr', 'dsgf', 'erght')
print(t)
tt = sorted(t, reverse = True)
print(tt)
var = sorted(t, key = lambda x : x[::-1]) # 从后面王前面排序
print(var)






