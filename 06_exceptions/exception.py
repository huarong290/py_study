# 运行时错误：异常通常在程序运行时发生，比如除以零、访问不存在的键。
# 类型丰富：Python 内置了很多异常类型，如 ZeroDivisionError、KeyError、ValueError。
# 可捕获：通过 try...except 语句捕获并处理。
# 可自定义：可以定义自己的异常类。

# 1. 基本异常处理
try:
    x = 10 / 0
except ZeroDivisionError:
    print("不能除以零！")

# 2. 捕获多个异常
try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print("发生错误:", e)

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("不能除以零！")
# except ValueError:
#     print("value error")
# except KeyError:
#     print("key error")

#3.使用 else 和 finally
try:
    result = 10 / 2
except ZeroDivisionError:
    print("除零错误")
else:
    print("计算成功:", result)
finally:
    print("无论是否出错都会执行")

# 4. 自定义异常
class MyError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise MyError("值不能为负数")

try:
    check_value(-5)
except MyError as e:
    print("捕获到自定义异常:", e)
