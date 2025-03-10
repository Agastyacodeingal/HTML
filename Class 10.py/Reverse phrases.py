word = input("enter a phrase") 
rev = ""
for i in word:
    rev = i+rev 
print("the reverse string is", rev)