# 用字典存储商品和价格
# List  tuple  Dict

cart_dict = {"苹果": 5}

for key in cart_dict.keys():
    print(key)
cart_dict_list = [{"苹果": 5},{"香蕉": 10},{"荔枝": 120}]
cart_dict_list2 = {"苹果": 5,"香蕉": 10,"荔枝": 120}
print(cart_dict_list)
print(cart_dict_list[0].keys())
print(cart_dict_list[0].values())
for key,value in  enumerate(cart_dict_list2):
    print(key,value)