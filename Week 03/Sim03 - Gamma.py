# Gamma Distribution
# ------------------------------
# PDF:
#   f(x) = (β^α * x^{α-1} * e^{-βx}) / Γ(α),   x > 0
#
# Mean:
#   E(X) = α / β
#
# Variance:
#   Var(X) = α / β²
#
# Std. Dev:
#   σ = sqrt(α) / β
# ------------------------------

from scipy.stats import gamma

# ================= Example 1 =================
# α = 2, β = 1 → Gamma(2, 1)
# Find P(X < 3)
# =============================================
alpha = 2
beta = 1
x = 3
scale = 1 / beta

prob = gamma.cdf(x, alpha, scale=scale)
mean = alpha / beta
variance = alpha / (beta ** 2)
std_dev = math.sqrt(alpha) / beta

print("Gamma Example 1")
print(f"P(X < {x}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")


# ================= Example 2 =================
# α = 3, β = 2 → Gamma(3, 2)
# Find P(X > 4)
# =============================================
alpha = 3
beta = 2
x = 4
scale = 1 / beta

prob = gamma.sf(x, alpha, scale=scale)
mean = alpha / beta
variance = alpha / (beta ** 2)
std_dev = math.sqrt(alpha) / beta

print("Gamma Example 2")
print(f"P(X > {x}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")


# ================= Example 3 =================
# α = 5, β = 1.5 → Gamma(5, 1.5)
# Find P(2 < X < 6)
# =============================================
alpha = 5
beta = 1.5
a, b = 2, 6
scale = 1 / beta

prob = gamma.cdf(b, alpha, scale=scale) - gamma.cdf(a, alpha, scale=scale)
mean = alpha / beta
variance = alpha / (beta ** 2)
std_dev = math.sqrt(alpha) / beta

print("Gamma Example 3")
print(f"P({a} < X < {b}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")
