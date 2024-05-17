import matplotlib.pyplot as plt
import glob
import os

file_paths = glob.glob('names/*.txt')

name_counts = {}

for file_path in file_paths:
    category = os.path.basename(file_path).split('.')[0]

    with open(file_path, 'r') as f:
        names = f.readlines()
        name_counts[category] = len(names)

plt.figure(figsize=(10, 6))
plt.bar(name_counts.keys(), name_counts.values())
plt.xlabel('Name Category')
plt.ylabel('Number of Names')
plt.title('Distribution of Names in PyTorch Dataset')
plt.xticks(rotation=45)  
plt.show()
