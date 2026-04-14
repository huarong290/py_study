#定量输出
from operator import truediv, floordiv

print("#########################")
print("######## 白日依山尽 #######")
print("######## 黄河入海流 #######")
print("######## 欲穷千里目 #######")
print("######## 更上一层楼 #######")
print("#########################")


#变量输出(变量定义时必须赋值才能使用,可一次定义多个变量)
num= 11306
print(num)

num = num + 1
print(num)

num = True
print(num)

#举例
base = 20.4
up = 48
print("最终数量=base+up*2")
print("最终数量 =",base+up*2)
#operator.truediv(a, b) 等价于 a / b
#operator.floordiv(a, b) 不同，floordiv 是整除（向下取整）
print(truediv(10, 4))   # 输出 2.5
print(10 / 4)           # 输出 2.5，效果相同

print(floordiv(7, 2))    # 输出 3
print(7 // 2)           # 输出 3，整除