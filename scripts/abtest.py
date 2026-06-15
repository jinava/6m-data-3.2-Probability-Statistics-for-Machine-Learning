import numpy as np
from scipy import stats

# 1. 模拟 A/B 测试的真实用户数据 (1代表点击，0代表未点击)
np.random.seed(42)
group_A = np.random.choice([0, 1], size=2000, p=[0.90, 0.10]) # 旧算法：10% 点击率
group_B = np.random.choice([0, 1], size=2000, p=[0.885, 0.115]) # 新算法：11.5% 点击率

# 计算两组的表面点击率
print(f"A组（旧算法）表现点击率: {np.mean(group_A)*100:.2f}%")
print(f"B组（新算法）表现点击率: {np.mean(group_B)*100:.2f}%")

# 2. 进行假设检验 (这里使用双样本独立 T 检验)
# H0: A组和B组的平均点击率没有区别
# H1: A组和B组的平均点击率有显著区别
t_stat, p_value = stats.ttest_ind(group_A, group_B, equal_var=False)

print(f"\n--- 假设检验法庭判决 ---")
print(f"计算出的 T 统计量 (T-statistic): {t_stat:.4f}")
print(f"计算出的 P 值 (P-value): {p_value:.4f}")

# 3. 做出决策
alpha = 0.05
if p_value < alpha:
    print("【判决结果】：P值小于0.05！拒绝原假设！")
    print("新算法的提升是【显著的】，排除运气成分，建议【立即全量上线】。")
else:
    print("【判决结果】：P值大于0.05！无法拒绝原假设。")
    print("虽然表面上有提升，但统计学认为这大概率是【随机波动造成的】，新算法【不予上线】。")

