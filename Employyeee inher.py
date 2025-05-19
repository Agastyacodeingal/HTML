class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class emp (person):
    def __init__(self, name,age,post):
        person. __init__(self,name,age)
        self.post = post
    def print_emp(self):
        print("The employee name is ",self.name)
        print("The employees age is ",self.age)
        print("The employees post is ",self.post)
e1 = emp("Brandon","36","Engineer")
e1.print_emp()