import myMath
import random
import datetime
print(myMath.add(3,4))
print(myMath.multiply(3,4))
random_list=[]

for _ in range(5):
    num = random.randint(1,10)
    random_list.append(num)

print(f"生成的随机列表为：{random_list}")


now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

