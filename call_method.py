class MyFunction:
    def __init__(self):
        pass

    def __call__(self, x, y):
        return x + y


# 创建一个实例
addition = MyFunction()

# 现在，我们可以像调用函数一样使用这个实例
result = addition(3, 5)
print(result)  # 输出: 8
