# Immutable objects

x = (1, 2)
y = x  # y is a copy of x
x = (1, 2, 3)

print(x, y)

# Mutable objects

a = [1, 2, 3]

b = a  # a and b are the same

a[0] = 100

print(a, b)
