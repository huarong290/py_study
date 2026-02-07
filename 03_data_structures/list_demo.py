# 功能需求
# 初始化购物清单：用一个列表存储商品。
# 添加商品：用户输入商品名，加入列表。
# 删除商品：用户输入商品名，从列表移除。
# 查看清单：打印当前所有商品。
# 退出程序：结束循环


product_list = []


while True :
    operator_input = input("请输入操作类型：1-添加商品 2-删除商品 3-查询商品列表 4退出 ")
    if not operator_input.isdigit():
        print("请输入数字 1~4")
        continue
    else:
        operator =int(operator_input)
        if operator == 1:
            product_name =input("请输入添加的商品：")
            product_list.append(product_name)
            print(product_list)
        elif operator == 2:
            product_name = input("请输入删除商品：")
            if len(product_list) == 0:
                print("当前没有可以删除的商品")
            else:
                if product_name not in product_list:
                    print("当前没有可以删除的目标商品")
                else:
                    product_list.remove(product_name)
                print(product_list)
        elif operator == 3:
            if len(product_list) == 0:
                print("当前购物清单为空")
            else:
                print("当前购物清单：")
                for i, item in enumerate(product_list, start=1):
                    print(f"{i}. {item}")
        elif operator == 4:
            print("正在退出")
            break
        else:
            print("不合法的输入")
print('程序结束')