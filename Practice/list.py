# list

squares = [1, 2, 5 , 6]
print(squares)

a = ["string", "test", 152]
print(a)
print(a[1:3])
print(a[-1])
print(a[0])
print(a[:])


cube = [1,2, 5, 65]
print(cube)
cube[3] = 4 ** 3
print(cube)
print(a + cube)
cube.append(5**4)
print(cube)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[0:2] = ['A', 'B', 'C']
print(letters)
letters[2:4] = []
print(len(letters))
print(letters)
letters[:] = []
print(letters)

n = [letters, squares]
print(n)
print(len(n))

