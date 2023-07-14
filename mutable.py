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


# side effect


def sort_numbers(numbers):
    numbers.sort()

    return numbers


nums = [2, 3, 4, 5, 1, 11, 9]

print(nums)

nums = sort_numbers(nums)

print(nums)
