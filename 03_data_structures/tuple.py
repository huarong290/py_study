# 创建元组
t = (1, 2, 3)
print(t[0])   # 输出 1
print(t[-1])  # 输出 3

# 元组不可修改
# t[0] = 10   # 会报错：TypeError: 'tuple' object does not support item assignment

# 元组可以包含不同类型
person = ("Tom", 20, True)
print(person)

# 元组解包
x, y, z = t
print(x, y, z)   # 输出 1 2 3

# 嵌套元组
nested = ((1, 2), (3, 4))
print(nested[0][1])   # 输出 2

# 元组和列表的区别
lst = [1, 2, 3]
lst[0] = 10   # 列表可以修改
print(lst)    # 输出 [10, 2, 3]
