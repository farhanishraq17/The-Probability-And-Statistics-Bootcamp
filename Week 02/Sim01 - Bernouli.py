from scipy.stats import bernoulli
import math

# ================================================================
# Example 1: Fair Coin Toss
# ------------------------------------------------
# Probability of success (Head) = 0.5
#
# Formula for Bernoulli Probability:
#     P(X = x) = p^x * (1 - p)^(1 - x)
#
# Expected Value:
#     E(X) = p
#
# Variance:
#     Var(X) = p * (1 - p)
#
# Standard Deviation:
#     σ = sqrt(Var(X))
# ================================================================

p = 0.5
x = 1   # success (Head)

prob = bernoulli.pmf(x, p)
mean = p
variance = p * (1 - p)
std_dev = math.sqrt(variance)

print("Example 1 - Coin Toss")
print(f"P(X=1): {prob:.2f}")
print(f"Expected Value (E[X]): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev:.4f}\n")


# ================================================================
# Example 2: Exam Pass Probability
# ------------------------------------------------
# Success (Pass) = 1, Failure (Fail) = 0
# Probability of success (p) = 0.8
#
# Formula:
#     P(X = x) = p^x * (1 - p)^(1 - x)
# ================================================================

p = 0.8
x = 0   # failure

prob = bernoulli.pmf(x, p)
mean = p
variance = p * (1 - p)
std_dev = math.sqrt(variance)

print("Example 2 - Exam Pass")
print(f"P(X=0): {prob:.2f} (probability of failing)")
print(f"Expected Value (E[X]): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev:.4f}\n")


# ================================================================
# Example 3: Machine Defect Test
# ------------------------------------------------
# Success = defective product (1)
# Failure = non-defective (0)
# Probability of success (p) = 0.1
#
# Formula:
#     P(X = x) = p^x * (1 - p)^(1 - x)
# ================================================================

p = 0.1
x = 0   # non-defective

prob = bernoulli.pmf(x, p)
mean = p
variance = p * (1 - p)
std_dev = math.sqrt(variance)

print("Example 3 - Machine Defect")
print(f"P(X=0): {prob:.2f} (probability of non-defective)")
print(f"Expected Value (E[X]): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev:.4f}")
