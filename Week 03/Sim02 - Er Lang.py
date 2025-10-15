# Erlang Distribution
# ------------------------------
# PDF:
#   f(x) = (λ^k * x^{k-1} * e^{-λx}) / (k-1)!
#
# Mean:
#   E(X) = k / λ
#
# Variance:
#   Var(X) = k / λ²
#
# Std. Dev:
#   σ = sqrt(k) / λ
# ------------------------------

from scipy.stats import erlang

# ================= Example 1 =================
# λ = 1, k = 2 → Erlang(2, 1)
# Find P(X < 3)
# =============================================
k = 2
lam = 1
x = 3
scale = 1 / lam  # in scipy, scale = 1/λ

prob = erlang.cdf(x, k, scale=scale)
mean = k / lam
variance = k / (lam ** 2)
std_dev = math.sqrt(k) / lam

print("Erlang Example 1")
print(f"P(X < {x}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")


# ================= Example 2 =================
# λ = 0.5, k = 3 → Erlang(3, 0.5)
# Find P(X > 5)
# =============================================
k = 3
lam = 0.5
x = 5
scale = 1 / lam

prob = erlang.sf(x, k, scale=scale)  # survival function P(X > x)
mean = k / lam
variance = k / (lam ** 2)
std_dev = math.sqrt(k) / lam

print("Erlang Example 2")
print(f"P(X > {x}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")


# ================= Example 3 =================
# λ = 2, k = 4 → Erlang(4, 2)
# Find P(1 < X < 3)
# =============================================
k = 4
lam = 2
a, b = 1, 3
scale = 1 / lam

prob = erlang.cdf(b, k, scale=scale) - erlang.cdf(a, k, scale=scale)
mean = k / lam
variance = k / (lam ** 2)
std_dev = math.sqrt(k) / lam

print("Erlang Example 3")
print(f"P({a} < X < {b}) = {prob:.6f}")
print(f"Mean = {mean}, Variance = {variance}, Std. Dev = {std_dev}\n")
