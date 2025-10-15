import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, erlang, gamma

# Normal Distribution Plot
mu = 100      # Mean
sigma = 15    # Standard deviation

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='blue', lw=2)
plt.title('Normal Distribution (μ=100, σ=15)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# Erlang Distribution Plot
k = 3       # shape parameter (integer)
lam = 1     # rate parameter
scale = 1 / lam

x = np.linspace(0, 15, 1000)
y = erlang.pdf(x, k, scale=scale)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='purple', lw=2)
plt.title('Erlang Distribution (k=3, λ=1)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# Gamma Distribution Plot
alpha = 5     # shape parameter
beta = 1.5    # rate parameter
scale = 1 / beta

x = np.linspace(0, 10, 1000)
y = gamma.pdf(x, alpha, scale=scale)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='green', lw=2)
plt.title('Gamma Distribution (α=5, β=1.5)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
