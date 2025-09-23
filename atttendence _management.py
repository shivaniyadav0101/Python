with open("attendence.txt","r")as f:
    file=f.read()
    student=set(file.splitlines())

with open("master.txt","r")as f2:
    file2=f2.read()
    present=set(file2.splitlines())
absent=student-present
print("present student",present)
print("absent student",absent)
#for writting a file for absent student 
with open("absent.txt","w")as f3:
    for roll in absent:
          f3.write(roll+"\n")


