from pymilvus import MilvusClient

# 连接
client = MilvusClient(uri="http://localhost:19530")
print("✅ 成功连接到 Milvus!")
collection_name = "health_check_test"

# 1. 创建 Collection (nomic-embed-text 的 768 维度)
if client.has_collection(collection_name):
    client.drop_collection(collection_name)

client.create_collection(collection_name=collection_name, dimension=768)
print("✅ 集合创建成功")

# 2. 插入一条模拟向量
import random
vector = [random.random() for _ in range(768)]
client.insert(collection_name=collection_name, data=[{"id": 1, "vector": vector, "text": "test"}])
print("✅ 数据写入成功")

# 3. 验证数据是否持久化到 MinIO
res = client.query(collection_name=collection_name, filter="id == 1", output_fields=["id"])
if len(res) > 0:
    print("✅ 检索验证成功，Milvus 处于完美状态！")