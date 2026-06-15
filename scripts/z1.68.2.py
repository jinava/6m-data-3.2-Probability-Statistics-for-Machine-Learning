import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'black', lw=2)

# Fill 68% area
x_fill = np.linspace(-1, 1, 100)
y_fill = norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.6)

plt.title('Standard Normal Distribution')
plt.show()

