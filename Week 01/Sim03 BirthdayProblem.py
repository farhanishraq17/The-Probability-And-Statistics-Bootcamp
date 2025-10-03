import random 
import math 

def exact_probability(n, days = 365):
    """Exact probability that at least two people share a birthday among n people."""
    if n > days : 
        return 1.0 # pigeonhole principle 
    
    #365 days 365 people jan 01 02 03 .... dec31 (consider its not a leap year)
    prob_all_distinct = 1.0 
   
    #how many of the elements are same?? 
    for k in range(n): 
        prob_all_distinct *= (days-k) / days 
    return 1 - prob_all_distinct #P(A) = 1 - P(not A)

def simulate_probability(n, trials = 100,days = 365):
    """Monte Carlo estimate of the birthday collision probability."""
    hits = 0 
    for _ in range(trials): 
        #generate n random birthdays (integers 0,1,2,3....)
        birthdays = [random.randrange(days) for _ in range(n)]
        # check if any duplicate exists
        
        if len(set(birthdays)) < n: 
            hits += 1
    return hits/trials

if __name__ == "__main__": 
    trials = 10000 
    interesting_ns = [5,10,20,23,30,50,60,70]
    print(f"Simulating {trials:,} trials per n (days=365)\n")
    
    print(f"{'n':>3}  {'Exact':>10}  {'Simulated':>10}")
    print("-" * 29)
    
    for n in interesting_ns:
        exact = exact_probability(n)
        sim = simulate_probability(n, trials=trials)
        print(f"{n:>3}  {exact:10.6f}  {sim:10.6f}")
    # Example: quick sweep to find smallest n with probability >= 0.5
    for n in range(1, 101):
        if exact_probability(n) >= 0.5:
            print(f"\nSmallest n with >=50% chance: n = {n} (exact = {exact_probability(n):.6f})")
            break
        
#What to expect

#Running the script with trials = 100000 will give 
#simulated probabilities close to the exact ones; they converge as trials grows.

#For n = 23 you should see something around 0.507 (the exact: ≈0.507297).

#The sweep will report n = 23 as the smallest 
#number of people with at least a 50% chance of a shared birthday.

