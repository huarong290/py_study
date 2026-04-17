#字典:使用键值对(key:value)来存储数据,每一个键都对应一个值,通过键(key)可以快速找到对应的值(value)
#特点:键值对(key:value)存储、键(key)不能重复、可修改。

# 定义字典
#字典名称={key: value, key:value, key:value ... }

# 定义空字典
#字典名称={}
#字典名称=dict()

# 根据key获取value
# 值 = 字典名称[key]
# dict1={"王林":670,"韩立":556,"李慕婉":582,"紫灵":435,"许立国":608,"王政":512,"张紫":678}

######  注意:字典(dict)中的value可以是任何类型的数据,而key不能为可变类型(如:不能为 列表list、集合set、字典dict)。

# 字典 -- key不能重复(如果重复,后面的值,会覆盖前面的值)、key必须得是不可变类型(str,int,float,tuple)
# 定义字典
dict1={"王林":670,"李慕婉":608,"徐立国":580,"韩立":688}
print(dict1)
print(type(dict1))


# key必须得是不可变类型(str,int,float,tuple),不能是list、set、dict
dict2 = {0:670, 1.5:608, (1,2):580, ('A' , 'B' ):688}
print(dict2)


# 访问
print(dict1["李慕婉"])  #获取
dict1["李慕婉"]=688   #value值可修改
print(dict1)





#------------------------------------------字典常用操作---------------------------------------
# 添加      字典名称[key]=value         往指定字典中添加key-value键值对                dict1["涛哥"]= 688
#
# 删除      字典名称.pop(key)           删除字典中指定的key,并返回该key对应的value      score=dict1.pop("涛哥")
#          del 字典名称[key]           删除字典中指定的键值对                         del dict1["涛哥"]
#
#修改       字典名称[key]= value        修改字典中指定的key对应的值                    dict1["小智"]= 658
#          字典名称[key]               根据key获取value                            dict1["涛哥"]
#          字典名称.get(key)           根据key获取value                            dict1.get("涛哥")
#
#查询       字典名称.keys()             获取所有的key                               dict1.keys()
#          字典名称.values()           获取所有的value                             dict1.values()
#          字典名称.items()            获取所有的key-value键值对                    dict1.items ()


#代码示例
dict1={"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"]=550
print(dict1)

# 修改 -key存在就是修改
dict1["涛哥"]=620
print(dict1)

# 查询
print(dict1["涛哥"])#根据key获取value
print(dict1.get("涛哥"))#根据key获取value
print(dict1.keys())#获取所有的key
print(dict1.values())#获取所有的value
print(dict1.items())#获取所有的键值对 key:value

# 删除
score=dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

# 遍历
for k in dict1.keys( ):
    print(f"{k} : {dict1[k]}")
for item in dict1.items( ):
    print(f"{item[0]} : {item[1]}")
for k,v in dict1.items():
    print(f"{k} : {v}")



#------------------------------------------案例----------------------------------------------
#需求:开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据,通过控制台菜单与用户交互。具体功能如下:
#1. 添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。
#2. 修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。
#3. 删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。
#4. 查询购物车:将购物车中的商品信息展示出来,格式为:“商品名称:xxx,商品价格:xxx,商品数量:xxx"。
#5. 退出购物车

dict={}

while True:
    menu = input("你想要执行哪项操作? 1.添加购物车 2.修改购物车 3.删除购物车 4.查询购物车 5.退出购物车: ")
    match  menu:
        case "1":
            shopping_name=input("请输入你要添加的商品名:")
            dict[shopping_name]={"价格":float(input("请录入商品的价格:")),"数量":int(input("请录入商品的数量:"))}
        case "2":
            shopping_name= input("请输入你要修改的商品名:")
            dict[shopping_name]= {"价格":float(input("请录入商品新的价格:")),"数量":int(input("请录入商品新的数量:"))}
        case "3":
            del dict [input("请输入你要删除的商品名:")]
        case "4":
            for shopping_name in dict.keys():
                shopping_passage=dict[shopping_name]
                shopping_price=shopping_passage["价格"]
                shopping_num=shopping_passage["数量"]
                print(f"商品名:{shopping_name},商品价格:{shopping_price},商品数量:{shopping_num}")
        case "5":
            break


# 字典推导式:--------------------------------------------------------------------
# 字典名称=[要插入字典的数据 for i in 字典 if 条件]

# 执行顺序（和列表推导式完全一致，从右到左执行）：
# ① 先执行 for 变量 in 可迭代对象：逐个取出元素
# ② 再执行 if 条件：筛选符合条件的元素（可选）
# ③ 最后执行 键: 值：对筛选后的元素生成键值对，放进新字典



# 一.模板 1：从单个可迭代对象生成字典（带筛选）
#          {键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
#
# 二.模板 2：从两个列表生成字典（最常用，AI 场景：标签 - 值映射）
#          {key: value for key, value in zip(键列表, 值列表)}
#
# 三.模板 3：从旧字典生成新字典（AI 场景：特征筛选 / 值转换）
#          {新键: 新值 for 旧键, 旧值 in 旧字典.items() if 条件}


from typing import Dict, List, Union
# ==================== 拆解1：带if条件的字典推导式（筛选） ====================
def create_even_square_dict() -> Dict[int, int]:
    """
    【拆解1】带if条件：生成1-10中偶数的平方字典
    语法：{键: 值 for 变量 in 可迭代对象 if 条件}
    """
    # 这行代码具体做了什么：
    #   ① 遍历1-10
    #   ② if num % 2 == 0：筛选偶数
    #   ③ 键是num，值是num的平方
    even_square_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
    return even_square_dict


# ==================== 拆解2：从两个列表生成字典（AI场景：标签-置信度映射） ====================
def create_label_confidence_dict(
        labels: List[str],
        confidences: List[float]
) -> Dict[str, float]:
    """
    【拆解2】从两个列表生成字典（最常用！）
    AI场景：把模型输出的“标签列表”和“置信度列表”合并成一个字典
    语法：{key: value for key, value in zip(键列表, 值列表)}
    """
    # 这行代码具体做了什么：
    #   ① zip(labels, confidences)：把两个列表“打包”成一对一对的（第2天学的zip()函数）
    #   ② for label, confidence in zip(...)：逐个取出每一对的键和值
    #   ③ 键是label，值是confidence
    # 是从哪来的：第2天学的zip()函数 + 字典推导式
    # 为什么要这么写：AI开发中，模型经常输出两个独立的列表，需要合并成字典方便后续处理
    label_confidence_dict = { label: confidence for label, confidence in zip(labels, confidences)}

    return label_confidence_dict


# ==================== 拆解3：从旧字典生成新字典（AI场景：特征筛选） ====================
def filter_feature_dict(
        raw_feature_dict: Dict[str, Union[int, float]],
        threshold: float = 0.5
) -> Dict[str, Union[int, float]]:
    """
    【拆解3】从旧字典生成新字典（AI场景：特征筛选）
    筛选出值大于threshold的特征，保留键，值保留2位小数
    语法：{新键: 新值 for 旧键, 旧值 in 旧字典.items() if 条件}
    """
    # 这行代码具体做了什么：
    #   ① 遍历旧字典的键值对（raw_feature_dict.items()）
    #   ② if value > threshold：筛选值大于阈值的特征
    #   ③ 新键是旧键（feature），新值是round(value, 2)（保留2位小数）
    filtered_feature_dict = {
        feature: round(value, 2)
        for feature, value in raw_feature_dict.items()
        if value > threshold
    }
    return filtered_feature_dict


# ==================== 测试所有示例 ====================
if __name__ == "__main__":

    # 测试拆解1：带if条件的偶数平方字典
    print(f"拆解1（偶数平方字典）：{create_even_square_dict()}\n")  # 输出：{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

    # 测试拆解2：从两个列表生成标签-置信度字典
    model_labels = ["猫", "狗", "鸟", "鱼"]
    model_confidences = [0.92, 0.87, 0.56, 0.34]
    print(f"拆解2标签列表：{model_labels}")
    print(f"拆解2置信度列表：{model_confidences}")
    print(f"拆解2合并结果：{create_label_confidence_dict(model_labels, model_confidences)}\n")
    # 输出：{'猫': 0.92, '狗': 0.87, '鸟': 0.56, '鱼': 0.34}

    # 测试拆解3：AI特征筛选
    raw_features = {"颜色": 0.89, "形状": 0.45, "纹理": 0.91, "大小": 0.32}
    print(f"拆解3原始特征：{raw_features}")
    print(f"拆解3筛选结果（阈值0.5）：{filter_feature_dict(raw_features)}")
    # 输出：{'颜色': 0.89, '纹理': 0.91}




# -------------------------------------生成器--------------------------------------------------
# 一、核心概念大白话解释
# 1.生成器表达式：Python 专门用来 **“用一行代码快速生成一个‘按需计算’的生成器对象”的语法，核心优势是极度节省内存 **，特别适合处理 AI 开发中的大文件、大数据集。

# 2.生活类比（核心：惰性求值）：
#   列表推导式：就像你去自助餐，一次性把所有菜都夹到盘子里，堆得满满当当，占了很大的桌面空间（内存），不管你吃不吃得完，都先夹过来。
#   生成器表达式：就像你去吃日式拉面，你点一碗，厨师才给你做一碗，吃完一碗再点下一碗，桌面上永远只有一碗面（几乎不占内存），按需制作，绝不浪费。

# 3.惰性求值特性（必须牢记）：生成器表达式不会立即计算所有结果，只是创建了一个 “生成器对象”，只有当你主动要结果的时候（用next()函数或者for循环遍历），
#                              它才会计算一个结果给你，算完一个就 “忘” 一个，绝不占用额外内存。




# 二、固定代码逻辑结构顺序（模板总结）
# 生成器表达式常见模板（后续可直接套用）

# 模板 1：带筛选的生成器
#   (表达式 for 变量 in 可迭代对象 if 条件)
#
# 模板 2：逐个获取结果（用 next ()）
#   gen = (表达式 for 变量 in 可迭代对象)
#   result1 = next(gen)  # 获取第一个结果
#   result2 = next(gen)  # 获取第二个结果
#
# 模板 3：遍历所有结果（用 for 循环，最常用）
#   gen = (表达式 for 变量 in 可迭代对象 if 条件)
#   for result in gen:
#       # 处理每个结果
#       print(result)
#
# 模板4：处理大文件（AI开发核心场景）
#     # 逐行读取大文件，绝不一次性加载整个文件到内存
#   with open("large_dataset.csv", "r", encoding="utf-8") as f:
#       # 生成器表达式：逐行处理，筛选有效数据
#       data_gen = (line.strip() for line in f if line.strip() != "")
#       for data in data_gen:
#           # 处理每一行数据
#           process(data)



# 代码示例:
# 导入类型注解模块和sys模块（用来查看内存占用）
from typing import Generator, List
import sys
# ==================== 拆解2：带if条件的生成器 ====================
def filter_even_squares() -> Generator[int, None, None]:
    """
    【拆解2】带if条件的生成器：筛选1-20的偶数的平方
    """
    # 这行代码具体做了什么：
    #   ① 遍历1-20
    #   ② if num % 2 == 0：筛选偶数
    #   ③ 表达式是num ** 2
    # 注意：此时不会计算任何结果！
    even_square_gen = (num ** 2 for num in range(1, 21) if num % 2 == 0)
    return even_square_gen


# ==================== 拆解3：AI开发核心场景：逐行处理大文件 ====================
def process_large_file(file_path: str) -> None:
    """
    【拆解3】AI开发核心场景：逐行处理大文件
    核心优势：绝不一次性加载整个文件到内存，哪怕文件有10GB也能处理
    模拟场景：读取大的CSV数据集，筛选有效数据行
    """
    # 这行代码具体做了什么：用with open()打开文件（安全，自动关闭）
    # 是从哪来的：Python文件操作基础
    with open(file_path, "r", encoding="utf-8") as f:
        # 这行代码具体做了什么：生成器表达式，逐行处理
        #   ① line.strip()：去除每行前后的空格和换行符
        #   ② for line in f：逐行读取文件（f本身就是可迭代对象，逐行读）
        #   ③ if line.strip() != ""：筛选掉空行
        # 注意：此时不会读取任何行！
        data_gen = (line.strip() for line in f if line.strip() != "")

        # 这行代码具体做了什么：用for循环遍历生成器，此时才逐行读取和处理
        print("开始逐行处理大文件：")
        for i, data in enumerate(data_gen, 1):
            print(f"处理第 {i} 行数据：{data}")
            # AI开发中，这里可以加数据预处理、模型推理等逻辑
            # 比如：process_data(data)


# ==================== 测试所有示例 ====================
if __name__ == "__main__":

    # 3. 测试带if的生成器
    print("=== 拆解2：带if条件的生成器 ===")
    even_square_gen = filter_even_squares()
    print("带if的生成器结果：")
    for num in even_square_gen:
        print(num, end=" ")  # 输出：4 16 36 64 100 144 196 256 324 400
    print("\n" + "=" * 50 + "\n")

    # 4. 测试大文件处理（先创建一个测试用的小文件）
    print("=== 拆解3：大文件处理 ===")
    # 先创建一个测试文件
    with open("test_large_file.csv", "w", encoding="utf-8") as f:
        f.write("数据1\n\n数据2\n数据3\n\n数据4\n")
    # 处理测试文件
    process_large_file("test_large_file.csv")


# 惰性求值的验证：生成器创建后不会立即计算，只有next()或for循环才会计算