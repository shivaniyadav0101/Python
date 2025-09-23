number=input("enter numbers ")
list1=list(map(int,number.split())) #split input string and convert to integers
unique=set(list1)
list2=sorted(list(unique))
#statistics
count=len(list2)
sum_values=sum(list2)
avarage=sum_values/count
largest=max(list2)
smallest=min(list2)
#output
print("count",count)
print("sum of list",sum_values)
print("avarage of list elements",avarage)
print("largest number",largest)
print("smallest number",smallest)

