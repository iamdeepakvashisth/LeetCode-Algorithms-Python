'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

'''

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        for i in range(1,len(nums)+1):
            s.add(i)
        return list(s-set(nums))