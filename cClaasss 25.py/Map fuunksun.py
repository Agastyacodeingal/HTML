#map fuction
n1 = [1,2,6,8,6]
n2 = [2,13,4,5,]

result  = map(lambda x,y:x+y,n1,n2)

print(list(result))

def sqr(x):
    return x*x

list1 = [12,34,56,78,90]

result = list(map(sqr,list1))

print(result)