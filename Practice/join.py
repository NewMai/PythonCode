
seq1 = ['hello','good','boy','doiido']
var = "-".join(seq1)
print(seq1)
print(var)
var = var.split("-")
print(var)
print()


seq2 = "hello good boy doiido"
print(seq2)
var = seq2.split(" ")
print(var)
var = "_".join(var)
print(var)
var = " ".join(var.split("_"))
var = ":".join(var)
print(var)
print()


seq3 = ('hello','good','boy','doiido')
var = "^".join(seq3)
print(var)
var = "...".join(seq3)
print(var)
print()

seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
var = "  ".join(seq4.keys())
print(var)
var = var.split("  ")
print(var)
r = seq4.values()
rr = list(r)
tmp = []
for x in rr:
	tmp.append(str(x))
rr = tmp
rr = ' '.join(rr)
print(rr)
print()









