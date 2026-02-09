# 函数的特点
# 定义：使用 def 关键字。
# 参数传递：支持位置参数、关键字参数、默认参数、可变参数。
# 返回值：用 return 返回结果，可以返回一个或多个值（通常是元组）。
# 作用域：函数内部的变量默认是局部变量，外部不可直接访问


# 1. 定义与调用
def great(name):
    print(f"Great!,{name}")
great('你好')

# 2. 带返回值
def add(a, b):
    return a + b
result = add(3, 5)
print(result)   # 输出 8

# 3. 默认参数
def power(base, exp=2):
    return base ** exp

print(power(3))      # 输出 9 (默认平方)
print(power(3, 3))   # 输出 27

# 4. 可变参数
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))   # 输出 10


# 5. 返回多个值（元组解包）
def divide(a, b):
    return a // b, a % b

q, r = divide(10, 3)
print(q, r)   # 输出 3 1
