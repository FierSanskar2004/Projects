import random
rand=random.randint(1,100)

guess=int(input("Enter your guess  : "))

while guess != rand:
    if guess>rand and guess!=0:
        guess=int(input("Wrong answer. Answer is lower than you think. Try again! (Type 0 to give up) : "))
    elif guess<rand and guess!=0:
        guess=int(input("Wrong answer. Answer is higher than you think. Try again! (Type 0 to give up) : "))
    elif guess == rand:
        print("Correct answer. You win.")   
    elif guess == 0:
        print("The correct answer is : ",rand)
        break
    else:
        print("Error! Game crashed!")
 


