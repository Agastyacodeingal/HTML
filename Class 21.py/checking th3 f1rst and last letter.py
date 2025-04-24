#checking the3 f1rst and last letter

def check (list1):
    temp = []
    count = 0
    for i in list1:
        if i[0] == i[-1]:
            count+=1
            temp. append(i)
        print("The no. of words which are same first and last are ")
    return temp
list1 = ['gibb','nib','knick','knack','bimb','bamb']

print(check(list))