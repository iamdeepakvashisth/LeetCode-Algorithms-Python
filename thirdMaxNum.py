'''
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

'''

def thirdMax(self, nums: List[int]) -> int:
    s=set(nums)
    if len(s)>=3:
        return sorted(list(s), reverse=True)[2]
    else:
        return max(s)