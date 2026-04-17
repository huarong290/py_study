#需求
#1. 定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。
#2. 定义一个函数:计算传入的字符串中元音字母的个数(元音字母为 aeiouAEIOU)。
#3. 定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数),并返回。

def  fun_area_of_triangle(  base , height ):
    return (base * height)/2
print(fun_area_of_triangle(3,3))

def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))
    if kwargs.get("print") :
        print(f"最大值为{max_data},最小值为{min_data},平均值为{avg_data}")
    return min_data, max_data, avg_data, kwargs.get("round")

data = calc_data(107, 112, 92, round=3, print=True) #--->round 是键名,3是键值,所以说**kwargs封装的是字典
print(data)

data = calc_data(33, 11, 28, 91, 32, 75, 49)   # 注意:此处调用函数时,没有传递kwargs字典值,则函数中不能用kwargs["round"]
print(data)                                          #  取值,这种方式会在没有值的时候报错,这里只能用kwargs.get("round"),这种
                                                     #  方式会在没有值的时候默认返回None,相比前者适配性更高