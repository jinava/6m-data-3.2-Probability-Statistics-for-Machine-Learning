import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. 模拟 30 天的退货率数据
np.random.seed(24)
days = np.arange(1, 31)

# 前 25 天属于正常波动（均值 3.2%，标准差 0.8%）
normal_days = np.random.normal(loc=3.2, scale=0.8, size=25)

# 后 5 天由于某种业务故障，退货率突然连续飙升
anomaly_days = np.array([4.2, 3.9, 5.6, 6.1, 5.8]) 

# 合并完整数据
return_rates = np.concatenate([normal_days, anomaly_days])
df = pd.DataFrame({'Day': days, 'Return_Rate': return_rates})

# 2. 计算控制图的核心统计量（基于历史正常基线：前25天）
mu = np.mean(normal_days)
sigma = np.std(normal_days)

UCL = mu + 3 * sigma
CL = mu
LCL = max(0, mu - 3 * sigma) # 下限不能为负数

print(f"--- SPC 控制图基线指标 ---")
print(f"控制上限 (UCL): {UCL:.2f}%")
print(f"中心线 (CL): {CL:.2f}%")
print(f"控制下限 (LCL): {LCL:.2f}%\n")

# 3. 自动检测异常点
df['Z_Score'] = (df['Return_Rate'] - mu) / sigma
df['Is_Anomaly'] = df['Return_Rate'] > UCL

# 打印出触发告警的天数
anomalies = df[df['Is_Anomaly']]
for idx, row in anomalies.iterrows():
    print(f"🚨 警报：第 {int(row['Day'])} 天数据异常！当前值: {row['Return_Rate']:.2f}%, Z分数: {row['Z_Score']:.2f}")

# 4. 开始绘制 SPC 控制图
plt.figure(figsize=(12, 6))

# 画出每日数据走势线
plt.plot(df['Day'], df['Return_Rate'], marker='o', color='#2c3e50', lw=2, label='Daily Return Rate')

# 画出三条核心控制线
plt.axhline(UCL, color='#e74c3c', linestyle='--', lw=2, label=f'UCL ({UCL:.2f}%)')
plt.axhline(CL, color='#2ecc71', linestyle='-', lw=1.5, label=f'CL / Mean ({CL:.2f}%)')
plt.axhline(LCL, color='#e74c3c', linestyle='--', lw=2, label=f'LCL ({LCL:.2f}%)')

# 高亮标出那些超越了 UCL 的异常点（变红）
plt.scatter(anomalies['Day'], anomalies['Return_Rate'], color='red', s=120, zorder=5, label='Anomaly Triggered')

# 装饰图表
plt.title('Product Daily Return Rate - SPC Control Chart (3-Sigma)', fontsize=14, pad=15)
plt.xlabel('Timeline (Days)', fontsize=12)
plt.ylabel('Return Rate (%)', fontsize=12)
plt.xticks(days)
plt.grid(axis='both', alpha=0.2)
plt.legend(loc='upper left')

# 显示图形
plt.show()

