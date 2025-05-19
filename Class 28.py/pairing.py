class pairofelements:
    def twosum(self,nums,target):
        sum = 0
        lookup = {}
        for i, sum in enumerate(nums):
            sum = sum+sum
            if sum>target:
                print("The index value is ",i)
                return
            lookup[nums] = i
p1 = pairofelements()
p1.twosum((10,20,30,40,100),60)