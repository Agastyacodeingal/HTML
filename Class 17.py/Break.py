#break


strl = input("Enter the string")

for i in strl: 
    if i.lower() == "a":
        print("A is found")
        break
    
        
else:
        print("A is not found")