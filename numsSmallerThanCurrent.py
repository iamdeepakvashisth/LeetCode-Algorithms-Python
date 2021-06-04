'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

'''

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if j != i and nums[j]<nums[i]:
                    count+=1
            res.append(count)
        return res