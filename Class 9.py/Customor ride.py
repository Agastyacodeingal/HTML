print("Enter your choice of vehicle \n1 Bike \n2 Car")
choice = int(input("Enter the choice of your vehicle"))
if choice == 1:
    print("Enter your choice of model \n1 scootie :) \n2 Yahmaha")
    choice2 = int(input("Enter the choice of your model"))
    if choice2 == 1:
        print("You selected scootie :)")
    else:
        print("You selected Yahmaha")
elif choice == 2:
    print("Enter your choice of model \n1 Hyundai \n2 Suzuki")
    choice2 = int(input("Enter the choice of your model"))
    if choice2 == 1:
        print("You selected Hyundai :)")
    else:
        print("You selected Suzuki")
else:
    print("Wrong option")