with open("C:\\Users\\Shivani\\story.txt","r")as f:
    r=f.read()
    r=r.lower()
    for i in [",",".","?",":",";"]:
        text=r.replace(i,"")
    para=text.split()
    dic={}
    for j in para:
        if j in dic:
            dic[j]+=1
        else:
            dic[j]=1
n=int(input("minimumu frequency:"))
for j in dic:
    if dic[j]>=n:
        print(j,dic[j])                    



