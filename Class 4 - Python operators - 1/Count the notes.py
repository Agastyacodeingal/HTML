#to count the no. of notes ._.
amt = int(input("Enter the amount of notes"))
note500 = amt//500
rem = amt%500
note100 = rem//100
rem = rem%100
note50 = rem//50
print("The number of 500 notes is",note500)
print("The number of 100 notes is",note100)
print("The number of 50 notes is",note50)