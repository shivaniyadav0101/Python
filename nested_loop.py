n=int(input("enter your value"))
#for i in range(n):
 #   for j in range(n-i):
  #      print("*",end="")

#for i in range(n):
 #  for j in range(i+1):
  #      print("*",end="")
   #  print()
count=0

#for i in range(n):
 #  for j in range(i+1):
  #     print(count+1,end="")
   #    count+=1
   #print()



#for i in range(n):
 #  for j in range(i+1):
  #     print(count+1,end="")
   #count+=1    
   #print()

#for i in range(n):
 #   if i<n/2:
  #      for j in range(i+1):
   #         print("*",end=" ")
    #else:
     #   for i in range(n-i):
      #      print("*",end=" ")
    #print()
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):#star
        print("*",end=" ")
    print()    
    
