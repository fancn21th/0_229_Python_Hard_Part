def some_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)
    pass


some_function(1, 2, 3)

some_function(arg3=3, arg2=2, arg1=1)


# *
def other_function(arg1, arg2, *args):
    print(arg1, arg2, args)
    pass


other_function(1, 2, 3, 4, 5)


# ** keyword arguments
def yet_another_function(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)
    pass


yet_another_function(1, 2, 3, 4, kwarg1=1, kwarg2=2, kwarg3=3)


# decompose a list
def decompose_list(a, b, c, e=True, f=False):
    print(a, b, c, e, f)
    pass


decompose_list(*[1, 2, 3], **{"e": True, "f": False})
