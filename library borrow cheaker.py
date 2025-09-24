books={"harry potter":2,"sherk":5,"gatha":6,"the conch bearer":4}
user=input("enter book to borrow")
if user in books and books[user]>0:
    books[user]-=1
    print("book isssued")
else:
    print("out of stock")
print("number of book ",books[user])
import json    
with open("library.txt","w")as f:
    json.dump(books,f)    