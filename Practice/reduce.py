#

a = [3,5,30,6,59,3,5,65,78,9,8,4,1,3,6,4,3]
print(a)
var = list(set(a))
print(var)
var.sort(key = lambda x : x%10) # 按照末位进行排序
print(var)
print()


var = dict.fromkeys(a)  # 利用 key 的唯一性
print(var)
var = var.keys()
print(var)
var = list(var)
print(var)
var = sorted(var)
print(var)
print()


var = a
print(var)
tmp = []
i = 1
for x in var:
	print("【%d】 count(%d) = %d"%(i, x, var.count(x)))
	if var.count(x)>1:
		#var.remove(x)
		print("Removing %d"%x)
	else:
		print("Adding new element %d"%(x,))
		tmp.append(x)
	i += 1
print(var)
var = sorted(tmp)
print(var)
for i,v in enumerate(var):
	print(i,v, var.count(v))
print()


s = "sdagradsfgharadfadfghsdaagd"
var = list(s)
var = set(var)
var = list(var)
print(s)
print(var)
var = "".join(var)
print(var)

print()



