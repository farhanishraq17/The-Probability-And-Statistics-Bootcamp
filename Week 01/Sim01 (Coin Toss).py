import random 
##################################################################
#P(A|B) = P(A ∩ B)/P(B)
# Probability of A given B is the probability of both A and B 
# happening divided by the probability of B happening.
##################################################################

# Event A ∩ B (both heads)
#Event B is at least one toss being head 
N = 1000000  # Number of simulations
count_A_and_B = 0  
count_B = 0
for _ in range(N):
    toss1 = random.choice(['H', 'T'])  # First coin toss
    toss2 = random.choice(['H', 'T'])  # Second coin toss

    if toss1 == 'H' or toss2 == 'H':  # Event B is at least one toss being head 
        count_B += 1
    if toss1 == 'H' and toss2 == 'H':  # Event A ∩ B (both heads)
        count_A_and_B += 1
            
prob = count_A_and_B / count_B 
print("Formula: P(A | B) = P(A ∩ B) / P(B)")
print (f"Probability of A given B (P(A|B)): {prob:.4f}")

