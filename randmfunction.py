import random
ran_number=random.randint(1,100)
user_number=int(input("enter your number"))
while user_number != ran_number:
    if user_number> ran_number:
        print("decrease your number")
    else:
        print("increase your number")
    user_number=int(input("enter your number"))    
print("congrate")        
