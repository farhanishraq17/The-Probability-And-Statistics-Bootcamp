# Exponential distribution examples
# --------------------------------
# Models waiting time between independent Poisson events with rate λ.
#
# PDF:
#    f(x) = λ * e^{-λ x},   x >= 0
#
# CDF:
#    F(x) = 1 - e^{-λ x}
#
# Survival (tail) prob:
#    P(X > x) = e^{-λ x}
#
# Mean:
#    E(X) = 1 / λ
#
# Variance:
#    Var(X) = 1 / λ^2
#
# Std. dev:
#    σ = 1 / λ
# --------------------------------

from scipy.stats import expon
import math

# Note: scipy.stats.expon uses the "scale" parameter = 1/λ

# ================= Example 1 =================
# Problem: Arrivals with rate λ = 0.5 per minute
# Mean waiting time = 1/λ = 2 minutes.
# Find probability waiting time ≤ 3 minutes: P(X ≤ 3).
# =============================================
lam = 0.5
x = 3.0
scale = 1.0 / lam  # scale = 1/λ

prob_le = expon.cdf(x, scale=scale)  # P(X ≤ x)
mean = 1.0 / lam
variance = 1.0 / (lam ** 2)
std_dev = 1.0 / lam

print("Exponential Example 1 - Arrival Wait")
print(f"P(X ≤ {x}) = {prob_le:.6f}")
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Std. Dev = {std_dev:.6f}\n")


# ================= Example 2 =================
# Problem: Component failure rate λ = 0.1 per year
# Find probability the component survives beyond 5 years: P(X > 5).
# (Survival probability = 1 - CDF = exp(-λ x))
# =============================================
lam = 0.1
x = 5.0
scale = 1.0 / lam

survival = expon.sf(x, scale=scale)  # survival = P(X > x)
mean = 1.0 / lam
variance = 1.0 / (lam ** 2)
std_dev = 1.0 / lam

print("Exponential Example 2 - Component Life")
print(f"P(X > {x}) = {survival:.6f}")
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Std. Dev = {std_dev:.6f}\n")


# ================= Example 3 =================
# Problem: Service time ~ Exponential with rate λ = 2 per hour
# Mean service time = 0.5 hour.
# Find probability service takes more than 0.5 hours: P(X > 0.5).
# =============================================
lam = 2.0
x = 0.5
scale = 1.0 / lam

survival = expon.sf(x, scale=scale)
mean = 1.0 / lam
variance = 1.0 / (lam ** 2)
std_dev = 1.0 / lam

print("Exponential Example 3 - Service Time")
print(f"P(X > {x}) = {survival:.6f}")
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Std. Dev = {std_dev:.6f}\n")
