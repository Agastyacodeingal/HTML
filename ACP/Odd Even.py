a = [2,1,3,45,54,32,3]
odd = []
even = []
for i in a:
    sqr = i*i
    if sqr%2==0:
        even.append(sqr)
    else:
        odd.append(sqr)
print(even)
print(odd)