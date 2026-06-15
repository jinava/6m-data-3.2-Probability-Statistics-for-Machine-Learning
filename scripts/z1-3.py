import numpy as np
from scipy.stats import norm

# 1. Generate data
np.random.seed(42)
data = np.random.normal(loc=0, scale=1, size=100000)

# 2. Count percentages
within_1_sd = np.sum((data >= -1) & (data <= 1)) / len(data) * 100
within_2_sd = np.sum((data >= -2) & (data <= 2)) / len(data) * 100
within_3_sd = np.sum((data >= -3) & (data <= 3)) / len(data) * 100

print(f"Z分数在 -1 到 +1 之间的数据占比: {within_1_sd:.2f}%")
print(f"Z分数在 -2 到 +2 之间的数据占比: {within_2_sd:.2f}%")
print(f"Z分数在 -3 到 +3 之间的数据占比: {within_3_sd:.2f}%")

