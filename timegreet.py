time=float(input("enter current time:"))
if time<12.00 and time>0:
    print("good morning")
elif time>=12.00 and time<17.00:
    print("good afternoon")
elif time<24 and time>17.00:
    print("good evening")
else:
    print("please enter valid timing")
    
    
