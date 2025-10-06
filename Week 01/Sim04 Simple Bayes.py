import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Setup Example: Defective Bulbs
# -------------------------------

# Suppose we have 3 machines producing bulbs
machines = ['B1', 'B2', 'B3']

# Probability that a bulb comes from each machine
P_B = [0.3, 0.4, 0.3]

# Probability that a bulb is defective given the machine
P_A_given_B = [0.01, 0.02, 0.03]

# --------------------------------
# 1. Total Law of Probability
# --------------------------------

# Theoretical total probability of a defective bulb
P_A = sum([P_B[i] * P_A_given_B[i] for i in range(len(P_B))])
print(f"Total probability of defect (theoretical): {P_A:.4f}")

# --------------------------------
# 2. Bayes Theorem
# --------------------------------

# Posterior probability: P(machine | defective)
P_B_given_A = [(P_A_given_B[i] * P_B[i]) / P_A for i in range(len(P_B))]

print("\nPosterior probabilities (Bayes Theorem):")
for i, prob in enumerate(P_B_given_A):
    print(f"Probability defective bulb came from {machines[i]}: {prob:.4f}")

# --------------------------------
# 3. Simulation using Random Sampling
# --------------------------------

np.random.seed(42)
N = 100000  # number of bulbs

# Step 1: Assign bulbs to machines based on prior probabilities
assigned_machines = np.random.choice(len(machines), size=N, p=P_B)

# Step 2: Simulate defective bulbs
defective = np.array([np.random.rand() < P_A_given_B[m] for m in assigned_machines])

# Step 3: Simulated probability of defect
sim_P_A = defective.mean()
print(f"\nSimulated probability of defect: {sim_P_A:.4f}")

# Step 4: Simulated posterior probability (Bayes)
sim_P_B_given_A = []
for m in range(len(machines)):
    sim_P_B_given_A.append(np.mean(assigned_machines[defective] == m))

print("\nSimulated posterior probabilities:")
for i, prob in enumerate(sim_P_B_given_A):
    print(f"Probability defective bulb came from {machines[i]}: {prob:.4f}")

# --------------------------------
# 4. Visualization
# --------------------------------

plt.figure(figsize=(12,5))

# Plot prior probabilities of machines
plt.subplot(1,2,1)
plt.bar(machines, P_B, color='skyblue')
plt.title("Prior Probabilities of Machines")
plt.ylabel("P(Bi)")

# Plot posterior probabilities using Bayes Theorem
plt.subplot(1,2,2)
plt.bar(machines, P_B_given_A, color='salmon', label='Theoretical')
plt.bar(machines, sim_P_B_given_A, color='yellowgreen', alpha=0.6, label='Simulated')
plt.title("Posterior Probabilities given Defective Bulb")
plt.ylabel("P(Bi|A)")
plt.legend()

plt.tight_layout()
plt.show()
