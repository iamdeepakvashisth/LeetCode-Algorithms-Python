'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''
def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        f=nums[:n]
        s=nums[n:]
        for i in range(len(f)):
            res.append(f[i])
            res.append(s[i])
        return res