def fac(a):
    result=1
    for i in range(1,a+1):
        if a>0:
            result*=i
        else:
            print("not valid number")
    print(result)        
n=int(input("enter number:"))
fac(n)    
