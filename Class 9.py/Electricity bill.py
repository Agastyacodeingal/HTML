units = int(input("Enter the units"))
if units <50:
    amount = units*2.60 + 25
elif units <100:
    amount = units*3.25 + 35
elif units<200:
    amount = units*5.26 + 45
else:
    amount = units*8.40 + 75
print("The electricity charges is ", amount)