#multipal exception

try:
    
    n1,n2 = eval(input("Enter 2 numbers seperated by commas"))
    
    result = n1/n2
    print (result)
except SyntaxError:
    print("Synthax Error")
    print("Comma is missing")
except ZeroDivisionError:
    print("Zero Division Error")
except:
    print("ValueError")
else:
    print("Everything is OK")
finally:
    print("It will work out even if an err0r is there")