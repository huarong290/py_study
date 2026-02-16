# 1.文件读取安全处理
# 写一个程序，尝试打开并读取文件 data.txt。
#
# 如果文件不存在，捕获异常并提示 "文件未找到"。
#
# 如果读取成功，打印文件内容
try:
    with open("data.txt", "r", encoding="utf-8") as fo:
        content = fo.read()
        print("文件内容如下：")
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("本次任务结束")

#2.除法函数
# 写一个函数 safe_divide(a, b)，返回 a / b。
# 如果 b == 0，捕获异常并返回 "不能除以零"。
# 否则返回结果

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("不能除以零")
result1= safe_divide(10,5)
print(result1)
safe_divide(10,0)

#3.自定义异常
# 定义一个异常类 NegativeValueError。
# 写一个函数 check_positive(x)：
# 如果 x < 0，抛出 NegativeValueError。
# 否则返回 "合法值"

class NegativeValueError(Exception):
    pass

def check_positive(x):
    if x < 0:
        raise NegativeValueError("x 不能小于 0")
    else:
        return x

num1 = check_positive(-10)

print(num1)