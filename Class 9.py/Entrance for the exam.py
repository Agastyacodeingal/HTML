mc = input("Enter the Medical cause y or n")
att = int(input("Enter the attendence"))
if mc=="y":
    print("Your allowed to enter")
else:
    if att>75:
        print("You are allowed to enter the exam")
    else:
        print("You are not allowed to enter the exam")