#fkxjlnhjc,

def flipflop (tuple1):
    length = len(tuple1)
    end = length-1
    start = 0
    
    while (start<end):
        if tuple1[start] != tuple1 [end]:
            return False
        start+=1 
        end-=1
        
        return True
    
tuple1 = (1,3,21,21,3,1)
if flipflop(tuple1):
    print(f"{tuple1} is a palladrome")
else:
    print(f"{tuple1} is not a palladrome")