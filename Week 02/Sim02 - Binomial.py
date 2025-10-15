from scipy.stats import binom
import math

# ================================================================
# Example 1: Coin Toss
# ------------------------------------------------
# A fair coin is tossed 10 times.
# Find the probability of getting exactly 6 heads.
# ------------------------------------------------
# Formula for Binomial Probability:
#     P(X = k) = C(n, k) * (p^k) * ((1 - p)^(n - k))
#
# Expected Value (Mean):
#     E(X) = n * p
#
# Variance:
#     Var(X) = n * p * (1 - p)
#
# Standard Deviation:
#     σ = sqrt(Var(X))
# ================================================================

n = 10      # number of trials
p = 0.5     # probability of success (head)
x = 6       # number of successes

prob = binom.pmf(x, n, p)
mean = n * p
variance = n * p * (1 - p)
std_dev = math.sqrt(variance)

print("Example 1 - Coin Toss")
print(f"P(X=6): {prob:.4f}")
print(f"Expected Value (E[X]): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev:.4f}\n")


# ================================================================
# Example 2: Defective Bulbs
# ------------------------------------------------
# A factory produces bulbs with 3% defect rate.
# Out of 20 bulbs, find probability that exactly 2 are defective.
# ------------------------------------------------
# Formula for Binomial Probability:
#     P(X = k) = C(n, k) * (p^k) * ((1 - p)^(n - k))
#
# Expected Value (Mean):
#     E(X) = n * p
#
# Variance:
#     Var(X) = n * p * (1 - p)
#
# Standard Deviation:
#     σ = sqrt(Var(X))
# ================================================================

n = 20
p = 0.03
x = 2

prob = binom.pmf(x, n, p)
mean = n * p
variance = n * p * (1 - p)
std_dev = math.sqrt(variance)

print("Example 2 - Defective Bulbs")
print(f"P(X=2): {prob:.6f}")
print(f"Expected Value (E[X]): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev:.4f}\n")


# ================================================================
# Example 3: Basketball Free Throws
# ------------------------------------------------
# A basketball player has a 70% chance of making a free throw.
# If they shoot 15 times, find the probability of making at least 10 baskets.
# ------------------------------------------------
# Formula for Binomial Probability:
#     P(X = k) = C(n, k) * (p^k) * ((1 - p)^(n - k))
#
# For "at least 10" successes:
#     P(X ≥ 10) = 1 - P(X ≤ 9)
#                = 1 - Σ [P(X = k)] for k = 0 to 9
#
# Expected Value (Mean):
#     E(X) = n * p
#
# Variance:
#     Var(X) = n * p * (1 - p)
#
# Standard Deviation:
#     σ = sqrt(Var(X))
# ================================================================

n = 15
p = 0.7

prob = 1 - binom.cdf(9, n, p)
mean = n * p
variance = n * p * (1 - p)
std_dev = math.sqrt(variance)

print("Example 3 - Free Throws")
print(f"P(X ≥ 10): {prob:.4f}")
print(f"Expected Value (E[X]): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev:.4f}")
