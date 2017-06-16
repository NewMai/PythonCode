#

t = 12345, 54231, 'hello'
print(t)
print(t[-1])
print(t[1])

u = t, (1,2,3,4)
print(u)
print(u[1])
#u[1] = (11,22)  # 元组不可修改

v = ([1,2,3], [4,5,6])
print(v)
v[0][1] = 1111   # 但是元组可以包含可以修改的对象
print(v)

empty = ()
singleton = 'hello',  # 这样定义一个包含一个 元素的元组
print(empty)
print(singleton)



