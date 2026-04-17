#案例1. 将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值、最大值 和 平均值。

num_list = []

for i in range(10):
    num = int(input("请输入一个数据:"))
    num_list.append(num)

print(num_list)
