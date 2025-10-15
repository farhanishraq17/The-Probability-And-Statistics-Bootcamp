from scipy.stats import geom
import math

# ================================================================
# GEOMETRIC DISTRIBUTION
# ------------------------------------------------
# Describes the probability that the first success occurs
# on the k-th trial.
#
# Formula for Probability Mass Function (PMF):
#     P(X = k) = (1 - p)^(k - 1) * p
#
# Expected Value (Mean):
#     E(X) = 1 / p
#
# Variance:
#     Var(X) = (1 - p) / (p^2)
#
# Standard Deviation:
#     σ = sqrt(Var(X))
# ================================================================


# ===================== Example 1 ================================
# Problem: A fair coin (p = 0.5)
# Find the probability that the first head appears on the 3rd toss
# ================================================================

p = 0.5        # Probability of success (head)
k = 3          # First success on 3rd toss

# Compute probability using scipy
prob = geom.pmf(k, p)

# Compute expected value, variance, std deviation
mean = 1 / p
variance = (1 - p) / (p ** 2)
std_dev = math.sqrt(variance)

# Print results
print("Example 1 - Coin Toss (First Head on 3rd Toss)")
print(f"P(X=3): {prob:.4f}")
print(f"Expected Value (E[X]) = {mean}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {std_dev:.4f}\n")


# ===================== Example 2 ================================
# Problem: A machine fails each day with probability 0.1
# Find probability that it fails for the first time on day 5
# ================================================================

p = 0.1
k = 5

prob = geom.pmf(k, p)
mean = 1 / p
variance = (1 - p) / (p ** 2)
std_dev = math.sqrt(variance)

print("Example 2 - Machine Failure on Day 5")
print(f"P(X=5): {prob:.4f}")
print(f"Expected Value (E[X]) = {mean}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {std_dev:.4f}\n")


# ===================== Example 3 ================================
# Problem: A company gets a positive email response with p = 0.2
# Find probability that the first reply comes after 4 emails (on 5th)
# ================================================================

p = 0.2
k = 5

prob = geom.pmf(k, p)
mean = 1 / p
variance = (1 - p) / (p ** 2)
std_dev = math.sqrt(variance)

print("Example 3 - Email Response on 5th Try")
print(f"P(X=5): {prob:.4f}")
print(f"Expected Value (E[X]) = {mean}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {std_dev:.4f}\n")
