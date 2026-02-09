# 列表的特点
# 有序：元素有固定顺序，可以通过索引访问。
#
# 可变：可以修改、添加、删除元素。
#
# 支持多类型：同一个列表里可以放不同类型的数据。
#
# 常用场景：存储一组数据、循环处理、动态修改。

# 创建列表
lst = [1, 2, 3, "hello", True]
print(lst)   # 输出 [1, 2, 3, 'hello', True]

# 访问元素
print(lst[0])    # 输出 1
print(lst[-1])   # 输出 True

# 修改元素
lst[1] = 20
print(lst)   # 输出 [1, 20, 3, 'hello', True]

# 添加元素
lst.append("new")
print(lst)   # 输出 [1, 20, 3, 'hello', True, 'new']

# 删除元素
lst.pop()    # 删除最后一个
print(lst)   # 输出 [1, 20, 3, 'hello', True]

del lst[0]   # 删除第一个
print(lst)   # 输出 [20, 3, 'hello', True]

# 切片
print(lst[1:3])   # 输出 ['hello', True]

# 遍历
for item in lst:
    print(item)

# 列表推导式
# [表达式 for 变量 in 可迭代对象 if 条件]
# 表达式：生成的元素内容
# 变量：循环中的临时变量
# 可迭代对象：如 range()、列表、字符串
# 条件（可选）：筛选元素
squares = [x**2 for x in range(5)]
print(squares)   # 输出 [0, 1, 4, 9, 16]
# 带条件筛选
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # 输出 [0, 2, 4, 6, 8]
# 字符串处理
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print(upper_words)   # 输出 ['APPLE', 'BANANA', 'CHERRY']
#嵌套循环
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)   # 输出 [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


# 用列表推导式生成 1–100 的所有偶数平方

result = [ N**2 for N in range(1,100) ]
print(result)
