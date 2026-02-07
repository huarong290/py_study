# 功能逻辑
# 定义商品字典：商品名作为键，价格作为值。
# 显示商品列表：遍历字典，打印所有商品和价格。
# 用户选择商品：输入要购买的商品名。
# 计算总价：把选择的商品价格累加。
# 退出并显示总价。


product_dict = {
    '苹果': 8000,
    '小米': 6000,
    '华为': 7000,
}

my_product_cart= []
my_total_price = 0
print(product_dict)

for key, value in product_dict.items():
    print(f'{key}的价格是{value}')

if True:
    product_name = input("请输入要购买的商品名:")
    if product_name in product_dict.items():
        for item in product_dict.items():
            my_product_cart.append(item)

if my_product_cart.items().__len__() != 0:
    for key, value in my_product_cart.items():
        my_total_price = my_total_price + value

print(f"我一共购买商品的金额是{my_total_price}")