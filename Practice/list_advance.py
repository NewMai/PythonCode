#

squares = []
for x in range(10):
	squares.append(x**2)
print(squares)

squares2 = [x**2 for x in range(10)]
print(squares2)

squares3 = [(x,y) for x in [1,2,3] for y in [3,1,2] if x>=y]
print(squares3)
squares3.sort(key = lambda p: p[0])
print(squares3)

print()
print()
print()

vec = [-4, -2, 0, 2 , 4]
var = [x * 2 for x in vec]
print(var)
var = [x  for x in vec if x >= 0]
print(var)
var = [abs(x) for x in vec]
print(var)

freshfruit = ['banana', 'loganberry', 'passion fruit', 'aaa']
var = [weapon.strip() for weapon in freshfruit]
print(var)

var = [(x, x**2) for x in range(6)]
print(var)

vecc = [[1,2,3],[4,5,6],[7,8,9]]
var = [y for x in vecc for y in x]
print(var)

from math import pi
var = [str(round(pi, i)) for i in range(1, 6)]
print(var)

matrix = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
]
var = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
print(var)


print(list(zip(*matrix)))

