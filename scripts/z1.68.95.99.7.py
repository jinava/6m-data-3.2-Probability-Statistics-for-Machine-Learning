import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# 1. 准备正态分布曲线的数据
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(12, 7))
plt.plot(x, y, 'black', lw=2.5, zorder=10)

# 2. 从外到内，一层层填充颜色
# 填充 3 个标准差内的区域 (-3 到 3) -> 浅灰色
x_3 = np.linspace(-3, 3, 500)
plt.fill_between(x_3, norm.pdf(x_3), color='#f1f2f6', alpha=1, label='Within 3 SD (~99.7%)')

# 填充 2 个标准差内的区域 (-2 到 2) -> 浅蓝色
x_2 = np.linspace(-2, 2, 500)
plt.fill_between(x_2, norm.pdf(x_2), color='#dfe4ea', alpha=1, label='Within 2 SD (~95.4%)')

# 填充 1 个标准差内的区域 (-1 到 1) -> 亮蓝色
x_1 = np.linspace(-1, 1, 500)
plt.fill_between(x_1, norm.pdf(x_1), color='#74b9ff', alpha=0.6, label='Within 1 SD (~68.3%)')

# 3. 画出核心的边界虚线
colors = ['#ff7675', '#0984e3', '#2d3436']
for sd, col in zip([1, 2, 3], colors):
    plt.axvline(-sd, color=col, linestyle='--', alpha=0.7, lw=1.5)
    plt.axvline(sd, color=col, linestyle='--', alpha=0.7, lw=1.5)

# 4. 🔥 在图上硬编码写上精确的百分比文字
plt.text(0, 0.20, "68.27%", horizontalalignment='center', fontsize=13, weight='bold', color='#2d3436')
plt.text(1.5, 0.04, "95.45%", horizontalalignment='center', fontsize=11, weight='bold', color='#0984e3')
plt.text(-1.5, 0.04, "95.45%", horizontalalignment='center', fontsize=11, weight='bold', color='#0984e3')
plt.text(2.5, 0.008, "99.73%", horizontalalignment='center', fontsize=9, weight='bold', color='#d63031')
plt.text(-2.5, 0.008, "99.73%", horizontalalignment='center', fontsize=9, weight='bold', color='#d63031')

# 5. 美化图表
plt.title('Empirical Rule (68-95-99.7) in Normal Distribution', fontsize=14, pad=15)
plt.xlabel('Z-score (Standard Deviations)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
plt.xlim(-4, 4)
plt.ylim(0, 0.45)
plt.grid(axis='x', alpha=0.2)
plt.legend(loc='upper right')

# 6. 显示图形
plt.show()

