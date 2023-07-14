# list_comprehensions

x = [i for i in range(10)]

print(x)

y = [i for i in range(10) if i % 2 == 0]

print(y)

a = [i**2 for i in range(10)]

print(a)

b = [[j for j in range(i + 1)] for i in range(3)]

print(b)
