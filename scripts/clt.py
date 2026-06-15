import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. 制造一个极度偏态的总体数据（例如：指数分布，模拟严重的贫富差距）
np.random.seed(42)
population = np.random.exponential(scale=10, size=100000)
true_mean = np.mean(population)

print(f"--- 总体数据的真实情况 ---")
print(f"总体的真实真实平均值 (True Mean): {true_mean:.4f}\n")

# 2. 模拟中心极限定理 (CLT) 的抽样过程
sample_size = 50       # 每次抽 50 个人 (n >= 30)
num_simulations = 10000 # 重复抽样 10,000 次

sample_means = []
for _ in range(num_simulations):
    # 随机抽样
    sample = np.random.choice(population, size=sample_size, replace=True)
    # 计算这一撮人的平均值，并存起来
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# 3. 计算这 10,000 个样本均值的统计量
clt_mean = np.mean(sample_means)
clt_std = np.std(sample_means) # 这就是标准误差 (Standard Error)

# 4. 根据最后一次抽样，计算 95% 置信区间 (Confidence Interval)
# 公式: 样本均值 +- 1.96 * 标准误差
last_sample_mean = sample_means[-1]
ci_lower = last_sample_mean - 1.96 * clt_std
ci_upper = last_sample_mean + 1.96 * clt_std

print(f"--- CLT 抽样与置信区间结果 ---")
print(f"1万次抽样均值的平均数: {clt_mean:.4f} (极其接近总体的真实平均值!)")
print(f"最后一次抽样的均值: {last_sample_mean:.4f}")
print(f"该样本的 95% 置信区间为: [{ci_lower:.4f}, {ci_upper:.4f}]")
if ci_lower <= true_mean <= ci_upper:
    print("验证成功：当前的置信区间【成功框住了】总体的真实平均值！")
else:
    print("遗憾：当前的区间漏掉了真实平均值（这有 5% 的可能发生）。")

# 5. 绘制图形对比
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 图1：原始总体的分布（像滑梯一样极度倾斜，完全不是正态分布）
ax1.hist(population, bins=100, color='#ff7675', edgecolor='black', alpha=0.7)
ax1.set_title('1. Original Population Distribution\n(Highly Skewed / Non-Normal)', fontsize=12)
ax1.set_xlabel('Value')
ax1.set_ylabel('Count')

# 图2：1万个样本均值的分布（奇迹发生：变成了极其漂亮的、对称的钟形正态分布！）
ax2.hist(sample_means, bins=100, density=True, color='#74b9ff', edgecolor='black', alpha=0.7, label='Sample Means')
# 叠加一条理论的正态分布曲线
x = np.linspace(clt_mean - 4*clt_std, clt_mean + 4*clt_std, 100)
ax2.plot(x, norm.pdf(x, clt_mean, clt_std), color='red', lw=2.5, label='Theoretical Normal Curve')
ax2.axvline(true_mean, color='black', linestyle='--', lw=2, label=f'True Mean ({true_mean:.2f})')
ax2.set_title('2. Distribution of 10,000 Sample Means\n(CLT in Action! Perfect Normal Distribution)', fontsize=12)
ax2.set_xlabel('Sample Mean Value')
ax2.set_ylabel('Probability Density')
ax2.legend()

plt.tight_layout()
plt.show()

