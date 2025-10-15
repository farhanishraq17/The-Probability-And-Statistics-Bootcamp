from scipy.stats import nbinom
import math

# ================================================================
# NEGATIVE BINOMIAL DISTRIBUTION
# ------------------------------------------------
# Models the number of trials needed to achieve r successes.
#
# Formula for Probability Mass Function (PMF):
#     P(X = k) = C(k-1, r-1) * (p^r) * (1 - p)^(k - r)
# where:
#     k = total number of trials (including the rth success)
#     r = number of required successes
#
# Expected Value (Mean):
#     E(X) = r / p
#
# Variance:
#     Var(X) = r * (1 - p) / (p^2)
#
# Standard Deviation:
#     σ = sqrt(Var(X))
#
# NOTE: In scipy's nbinom.pmf, the random variable represents the
# number of FAILURES before the r-th success, not total trials.
# Hence, we use (k - r) inside the PMF.
# ================================================================


# ===================== Example 1 ================================
# Problem: A fair coin (p = 0.5)
# Find probability that the 3rd head appears on the 5th toss
# ================================================================

r = 3          # Number of required successes
p = 0.5        # Probability of success
k = 5          # Total number of trials until 3rd success

# Calculate probability using scipy (k - r = number of failures)
prob = nbinom.pmf(k - r, r, p)

# Compute statistics
mean = r / p
variance = r * (1 - p) / (p ** 2)
std_dev = math.sqrt(variance)

# Print results
print("Example 1 - 3 Heads by 5th Toss")
print(f"P(X=5): {prob:.4f}")
print(f"Expected Value (E[X]) = {mean}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {std_dev:.4f}\n")


# ===================== Example 2 ================================
# Problem: Probability of passing an exam = 0.6
# Find probability that the 4th pass occurs on the 6th attempt
# ================================================================

r = 4
p = 0.6
k = 6

prob = nbinom.pmf(k - r, r, p)
mean = r / p
variance = r * (1 - p) / (p ** 2)
std_dev = math.sqrt(variance)

print("Example 2 - 4th Pass on 6th Exam")
print(f"P(X=6): {prob:.4f}")
print(f"Expected Value (E[X]) = {mean}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {std_dev:.4f}\n")


# ===================== Example 3 ================================
# Problem: A machine produces a working product with p = 0.8
# Find probability that the 5th working product occurs on 7th trial
# ================================================================

r = 5
p = 0.8
k = 7

prob = nbinom.pmf(k - r, r, p)
mean = r / p
variance = r * (1 - p) / (p ** 2)
std_dev = math.sqrt(variance)

print("Example 3 - 5th Working Product on 7th Trial")
print(f"P(X=7): {prob:.4f}")
print(f"Expected Value (E[X]) = {mean}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {std_dev:.4f}")
