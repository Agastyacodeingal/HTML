Marks1 = int(input("Enter the first marks"))
Marks2 = int(input("Enter the second marks"))
Marks3 = int(input("Enter the third marks"))
Marks4 = int(input("Enter the fourth marks"))
Marks5 = int(input("Enter the fifth marks"))
t = Marks1 + Marks2 + Marks3 + Marks4 + Marks5
avg  = t/5
if avg>90:
    print("GradeA")
elif avg>80:
    print("GradeB")
elif avg>70:
    print("GradeC")
elif avg>60:
    print("GradeD")
else:
    print("GradeE")