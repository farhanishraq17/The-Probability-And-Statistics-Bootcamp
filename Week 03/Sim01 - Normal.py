# Normal (Gaussian) Distribution
# ------------------------------
# PDF:
#   f(x) = (1 / (σ√(2π))) * exp(-0.5 * ((x - μ) / σ)^2)
#
# Mean:
#   E(X) = μ
#
# Variance:
#   Var(X) = σ²
#
# Std. Dev:
#   σ = standard deviation
# ------------------------------

from scipy.stats import norm
import math

# ================= Example 1 =================
# Heights of people ~ N(μ = 170, σ = 10)
# Find P(X < 180)
# =============================================
mu = 170
sigma = 10
x = 180

prob = norm.cdf(x, mu, sigma)  # P(X < x)
mean = mu
variance = sigma**2
std_dev = sigma

print("Normal Example 1 - Heights")
print(f"P(X < {x}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")


# ================= Example 2 =================
# IQ scores ~ N(μ = 100, σ = 15)
# Find P(85 ≤ X ≤ 115)
# =============================================
mu = 100
sigma = 15
a, b = 85, 115

prob = norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma)
mean = mu
variance = sigma**2
std_dev = sigma

print("Normal Example 2 - IQ Scores")
print(f"P({a} ≤ X ≤ {b}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")


# ================= Example 3 =================
# Exam marks ~ N(μ = 50, σ = 8)
# Find P(X > 60)
# =============================================
mu = 50
sigma = 8
x = 60

prob = 1 - norm.cdf(x, mu, sigma)  # P(X > x)
mean = mu
variance = sigma**2
std_dev = sigma

print("Normal Example 3 - Exam Marks")
print(f"P(X > {x}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")
