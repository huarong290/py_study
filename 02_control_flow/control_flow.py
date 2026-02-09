# 1. 条件判断：if / elif / else
x = 10
if x > 0:
    print("正数")
elif x == 0:
    print("零")
else:
    print("负数")

# 2. 循环：for
for i in range(5):
    print(i)
# 输出 0 1 2 3 4

# 3. 循环：while
n = 3
while n > 0:
    print(n)
    n -= 1
# 输出 3 2 1

# 4. 跳出与继续：break / continue
for i in range(5):
    if i == 3:
        break   # 提前结束循环
    print(i)
# 输出 0 1 2

for i in range(5):
    if i == 3:
        continue   # 跳过本次循环
    print(i)
# 输出 0 1 2 4
