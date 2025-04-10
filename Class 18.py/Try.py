#try

try:
    n = int(input("Enter the number"))
    print(n)
except ValueError as e:
    print(e)