#Armstrong loop
n = int(input("Enter the number"))
t=n
s=0 
while t>0:
    r = t%10
    s = s+r**3
    t//=10
print(s)
if s == n:
    print(n,"Is an Armstrong number")
else:
    print(n,"Is not an Armstrong number")