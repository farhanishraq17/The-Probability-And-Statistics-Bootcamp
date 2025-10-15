# Poisson distribution examples
# --------------------------------
# Models the number of events in a fixed interval when events occur
# independently at a constant average rate.
#
# PMF:
#    P(X = k) = (λ^k * e^{-λ}) / k!
#
# Mean:
#    E(X) = λ
#
# Variance:
#    Var(X) = λ
#
# Std. dev:
#    σ = sqrt(λ)
# --------------------------------

from scipy.stats import poisson
import math

# ================= Example 1 =================
# Problem: Average 3 emails per hour (λ = 3).
# Find probability of exactly 5 emails in an hour: P(X = 5).
# =============================================
lam = 3.0  # λ
k = 5      # observed count

prob = poisson.pmf(k, lam)  # P(X = 5)
mean = lam
variance = lam
std_dev = math.sqrt(lam)

print("Poisson Example 1 - Emails")
print(f"P(X = {k}) = {prob:.6f}")
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Std. Dev = {std_dev:.6f}\n")


# ================= Example 2 =================
# Problem: Calls arrive with average 0.2 calls per minute (λ = 0.2).
# Find probability of at most 2 calls in a minute: P(X ≤ 2).
# =============================================
lam = 0.2
k = 2

prob_cum = poisson.cdf(k, lam)  # P(X ≤ 2)
mean = lam
variance = lam
std_dev = math.sqrt(lam)

print("Poisson Example 2 - Calls")
print(f"P(X ≤ {k}) = {prob_cum:.6f}")
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Std. Dev = {std_dev:.6f}\n")


# ================= Example 3 =================
# Problem: On average 2 defects per batch (λ = 2).
# Find probability of zero defects: P(X = 0).
# =============================================
lam = 2.0
k = 0

prob = poisson.pmf(k, lam)  # P(X = 0)
mean = lam
variance = lam
std_dev = math.sqrt(lam)

print("Poisson Example 3 - Defects")
print(f"P(X = {k}) = {prob:.6f}")
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Std. Dev = {std_dev:.6f}\n")
