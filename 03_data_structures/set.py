# 创建集合
s = {1, 2, 3, 3}
print(s)   # 输出 {1, 2, 3} 自动去重

# 添加元素
s.add(4)
print(s)   # 输出 {1, 2, 3, 4}

# 删除元素
s.remove(2)
print(s)   # 输出 {1, 3, 4}

# 判断元素是否存在
print(3 in s)   # 输出 True

# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # 并集 {1, 2, 3, 4, 5}
print(a & b)   # 交集 {3}
print(a - b)   # 差集 {1, 2}
print(a ^ b)   # 对称差集 {1, 2, 4, 5}

# 使用 set() 去重
lst = [1, 2, 2, 3, 3, 4]
unique = set(lst)
print(unique)   # 输出 {1, 2, 3, 4}
