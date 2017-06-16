#

tel = {'jack': 123456, 'john': 555555}
print(tel)
#print(*tel.values())

tel["guidoe"] = 4444444
print(tel)
print(tel["john"])

print(tel.keys())
print(tel.values())

print(*tel.keys())
print(*tel.values())

print('jack' in tel)

info = dict([('a', 1),('b', 2), ('c', 3)])
print(info)


var = {x:x**3 for x in [1,5,9]}
print(var)
print(var[5])
print(var[9])



