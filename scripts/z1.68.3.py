import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# 重新生成曲线数据
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'black', lw=2)

# 1. 填充 -1 到 1 的蓝色区域
x_fill = np.linspace(-1, 1, 100)
y_fill = norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.6)

# 2. 🔥 核心核心：在图中央添加“百分比”文字标签
# 参数含义：x轴坐标=0, y轴坐标=0.18, 文字内容, 居中对齐, 字号, 加粗
plt.text(0, 0.18, "68.27%", horizontalalignment='center', fontsize=14, weight='bold', color='black')

# 3. 添加辅助虚线，指明 -1 和 1 的边界
plt.axvline(-1, color='red', linestyle='--', alpha=0.5)
plt.axvline(1, color='red', linestyle='--', alpha=0.5)

plt.title('Standard Normal Distribution')
plt.show()

