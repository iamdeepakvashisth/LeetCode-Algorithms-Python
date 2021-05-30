'''1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''
def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        sumOfElements=0
        for i in nums:
            sumOfElements+=i
            res.append(sumOfElements)
        return res