import random 

N = 10000

count_A_and_B = 0 # roll  is 6
count_B = 0 # roll is even

for _ in range(N): 
    roll = random.randint(1,6)
    
    if roll % 2 == 0: 
        count_B += 1
    if roll == 6: 
        count_A_and_B += 1

prob = count_A_and_B / count_B
print("P(Roll = 6 | Even) = ", prob)