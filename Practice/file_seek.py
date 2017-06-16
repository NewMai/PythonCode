#

f = None
with open("3333.txt", "w") as ff:
#f.close()

f = open("3333.txt", "r+")
f.write("123456789aaaaaa")
f.seek(0)
var = f.read(5)
print(var)

f.seek(6)
var = f.read(4)
print(var)

f.seek(2, 0)
var = f.read(4)
print(var)
f.close()


