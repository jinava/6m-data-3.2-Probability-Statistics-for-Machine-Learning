import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. 随机生成 100,000 个符合标准正态分布（均值0，标准差1）的数据点
np.random.seed(42)  # 固定随机种子以确保结果可复现
data = np.random.normal(loc=0, scale=1, size=100000)

# 2. 实际统计数据落在不同 Z 分数区间内的百分比
within_1_sd = np.sum((data >= -1) & (data <= 1)) / len(data) * 100
within_2_sd = np.sum((data >= -2) & (data <= 2)) / len(data) * 100
within_3_sd = np.sum((data >= -3) & (data <= 3)) / len(data) * 100

print(f"--- 10万个随机数据点的真实统计结果 ---")
print(f"Z分数在 -1 到 +1 之间的数据占比: {within_1_sd:.2f}% (理论值约 68%)")
print(f"Z分数在 -2 到 +2 之间的数据占比: {within_2_sd:.2f}% (理论值约 95%)")
print(f"Z分数在 -3 到 +3 之间的数据占比: {within_3_sd:.2f}% (理论值约 99.7%)")

# 3. 绘制正态分布曲线与面积填充
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'black', lw=2, label='Normal Distribution Curve')

# 填充 -1 到 +1 之间的面积（即 68% 的区域）
x_fill = np.linspace(-1, 1, 100)
y_fill = norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.6, label='Area between Z = -1 and +1 (~68%)')

# 装饰图表
plt.title('Standard Normal Distribution & 68% Empirical Rule Area', fontsize=14)
plt.xlabel('Z-score (Standard Deviations from Mean)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.axvline(0, color='gray', linestyle='--', label='Mean (Z=0)')
plt.xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
plt.legend(loc='upper right')
plt.grid(axis='x', alpha=0.3)

# 显示图表
plt.show()

