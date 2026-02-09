# 模块的特点
# 本质：一个 .py 文件就是一个模块。
# 复用性：写好的函数和类可以在不同程序中导入使用。
# 命名空间：模块提供独立的命名空间，避免变量冲突。
# 标准库：Python 自带大量模块（如 math、random、os）
# 常用标准库模块
# math：数学函数（平方根、三角函数、常数 π）。
# random：随机数生成。
# os：操作系统接口（文件路径、环境变量）。
# sys：Python 解释器相关信息。
# datetime：日期和时间处理。

# 1. 导入整个模块
import math
print(math.sqrt(16))   # 输出 4.0

# 2. 导入模块中的部分内容
from math import sqrt, pi
print(sqrt(25))   # 输出 5.0
print(pi)         # 输出 3.141592653589793

# 3. 给模块起别名
import random as rnd
print(rnd.randint(1, 10))   # 输出 1 到 10 的随机整数






