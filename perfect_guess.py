import random    
n=random.randint(1,100)
user=0
guess=1
while(user != n ):
    user = int(input("Guess a number: "))
    if(user >n ):
        print("Move to a lower Number")
        guess +=1
    elif(user<n):
        print ("Move to a Higher Number")
        guess +=1

print("You found the number in", guess , "tries !")