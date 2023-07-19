a = "".join(["a", "b", "c"])

b = "a" + "b" + "c"

c = "abc"

# Intern

print(a is b)  # False
print(a is c)  # False
print(b is c)  # True
