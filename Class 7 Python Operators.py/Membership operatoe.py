x = 25
if type (x) is int:
    print("True")
else:
    print("False")
y = 12.5
if type (y) is not float:
    print("False")
else:
    print("True")
a = 20
b = 24
if a is b:
    print("a and b are of same identity")
c = a
if a is c:
    print("a and c are of identity")