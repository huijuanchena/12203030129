import matplotlib.pyplot as plt
import glob
import os

# 获取所有文件路径
file_paths = glob.glob('names/*.txt')

# 创建一个字典来存储每个类别的名称和对应的数量
name_counts = {}

# 遍历每个文件并统计每个类别的数量
for file_path in file_paths:
    # 获取类别名称
    category = os.path.basename(file_path).split('.')[0]

    # 读取文件并计算每个类别的数量
    with open(file_path, 'r') as f:
        names = f.readlines()
        name_counts[category] = len(names)

# 可视化数据
plt.figure(figsize=(10, 6))
plt.bar(name_counts.keys(), name_counts.values())
plt.xlabel('Name Category')
plt.ylabel('Number of Names')
plt.title('Distribution of Names in PyTorch Dataset')
plt.xticks(rotation=45)  # 旋转类别名称，以防止重叠
plt.show()