import numpy as np
# 创建数组
arr_list = np.array([1, 2, 3, 4, 5])
print("数组:", arr_list)
# 创建随机矩阵
A = np.random.randint(1, 10, (3, 3))
print("矩阵A:\n", A)

# print("A.转置:\n", A.T)

# 矩阵点积
B= np.random.randint(1, 10, (3, 3))
print("矩阵 B:\n", B)
print("A 与 B 的点积:\n", np.dot(A, B))


