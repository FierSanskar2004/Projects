import random as abc

ct=0
ttl=0
t=int(input("No of times the coin will be flipped - "))

for i in range(1,t+1):
    ct=abc.randint(0,1)
    ttl+=ct
    print(f"No of heads = {ttl} No of tails = {i-ttl}")


print(f"Observed P(H) = {ttl/t} \nObserved P(T) = {1-(ttl/t)}")
print("Theoretical P(H) = 0.5 \nTheoretical P(T) = 0.5")