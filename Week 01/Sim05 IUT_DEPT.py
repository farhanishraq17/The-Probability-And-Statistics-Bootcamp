import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# IUT Departments
# -------------------------------
departments = ['CSE', 'EEE', 'MPE', 'BTM', 'CEE']
num_departments = len(departments)

# Prior probability: probability a student belongs to a department
# Example: adjust according to real data if available
P_Department = [0.3, 0.25, 0.2, 0.15, 0.1]

# Probability of passing the probability exam given department
P_Pass_given_Department = [0.85, 0.8, 0.75, 0.7, 0.65]

# -------------------------------
# 1. Total Probability of Passing
# -------------------------------
P_Pass = sum([P_Department[i] * P_Pass_given_Department[i] for i in range(num_departments)])
print(f"Total probability that a randomly selected student passes: {P_Pass:.4f}")

# -------------------------------
# 2. Bayes Theorem: Department given Passed
# -------------------------------
P_Department_given_Pass = [(P_Pass_given_Department[i] * P_Department[i]) / P_Pass for i in range(num_departments)]

print("\nProbability that a student belongs to a department given they passed:")
for i, prob in enumerate(P_Department_given_Pass):
    print(f"{departments[i]}: {prob:.4f}")

# -------------------------------
# 3. Simulation with Random Sampling
# -------------------------------
np.random.seed(42)
N = 200000  # number of students

# Assign students to departments
assigned_departments = np.random.choice(num_departments, size=N, p=P_Department)

# Simulate pass/fail based on department probabilities
passed = np.array([np.random.rand() < P_Pass_given_Department[d] for d in assigned_departments])

# Simulated probability of passing
sim_P_Pass = passed.mean()
print(f"\nSimulated probability of passing: {sim_P_Pass:.4f}")

# Simulated posterior probabilities (Bayes)
sim_P_Department_given_Pass = [np.mean(assigned_departments[passed] == d) for d in range(num_departments)]

print("\nSimulated probability department given passed:")
for i, prob in enumerate(sim_P_Department_given_Pass):
    print(f"{departments[i]}: {prob:.4f}")

# -------------------------------
# 4. Visualization
# -------------------------------
plt.figure(figsize=(14,6))

# Prior probabilities of departments
plt.subplot(1,2,1)
plt.bar(departments, P_Department, color='skyblue')
plt.title("Prior Probability of Departments")
plt.ylabel("P(Department)")

# Posterior probabilities: Theoretical vs Simulated
plt.subplot(1,2,2)
plt.bar(departments, P_Department_given_Pass, color='salmon', width=0.4, align='center', label='Theoretical')
plt.bar(departments, sim_P_Department_given_Pass, color='yellowgreen', width=0.4, align='edge', alpha=0.6, label='Simulated')
plt.title("Posterior Probability of Departments given Passed")
plt.ylabel("P(Department | Passed)")
plt.legend()

plt.tight_layout()
plt.show()
