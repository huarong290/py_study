# 字典的特点
# 键值对存储：每个元素由 key: value 组成。
# 键唯一：同一个字典里不能有重复的键。
# 无序（Python 3.7+ 实际上保持插入顺序，但逻辑上仍视为无序）。
# 可变：可以增删改。
# 键类型要求：键必须是不可变类型（如字符串、数字、元组），不能用列表或集合


# 创建字典
student = {"name": "Tom", "age": 20, "score": 95}
print(student)   # 输出 {'name': 'Tom', 'age': 20, 'score': 95}

# 访问值
print(student["name"])   # 输出 Tom
print(student.get("age"))   # 输出 20

# 修改值
student["age"] = 21
print(student)   # 输出 {'name': 'Tom', 'age': 21, 'score': 95}

# 添加新键值对
student["major"] = "Computer Science"
print(student)

# 删除键值对
del student["score"]
print(student)

# 遍历字典
for key, value in student.items():
    print(key, ":", value)

# 检查键是否存在
if "name" in student:
    print("存在 name 键")

# 使用字典推导式
squares = {x: x**2 for x in range(5)}
print(squares)   # 输出 {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
