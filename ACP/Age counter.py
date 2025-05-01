#Age counter

try:
    ch = input("Enter the Charecter")
    print(ch)
except ValueError as e:
    print(e)
    
if ch<3  ch>5:
    print("Even")
else:
    print("odd")