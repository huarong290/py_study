# 游戏逻辑
# 生成随机数：用 random.randint(1, 100) 生成一个 1 到 100 的随机整数。
# 循环输入：提示玩家输入一个数字。
# 比较大小：
# 如果输入比目标数大，提示“太大了”。
# 如果输入比目标数小，提示“太小了”。
# 如果输入等于目标数，提示“恭喜猜对了”，并结束游戏。
# 错误处理：如果输入不是数字，提示重新输入。
# 计数：可以记录玩家尝试的次数，最后输出总共用了多少次
# 进阶版玩法（比如“玩家有 10 次机会，失败后显示正确答案”）
import random

target = random.randint(1, 100)
chance_count = 10
count =0
while True:
    num = input("请输入一个整数: ")
    print(num)
    count = count + 1
    if not num.isdigit():
        print("输入不是数字，提示重新输入")
    else:
        num2 = int(num)
        if num2 > target:
            print("太大了")
        elif num2 < target:
            print("太小了")
        else:
            # 用逗号分隔（print 会自动转换为字符串并加空格）
            print('恭喜你在', count, '次数猜对了数字', num2)
            print(f'恭喜你在{count}次尝试猜对了数字{num2}')
            break
    if count >= chance_count:
        print(f"你的次数已经用完了,正确答案是{target}")
        break

