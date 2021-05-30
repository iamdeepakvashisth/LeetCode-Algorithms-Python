'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
'''
def searchRange(self, nums: List[int], target: int) -> List[int]:
        fisrtIndex,lastindex=-1,-1
        for i in range(len(nums)):
            if nums[i]==target and fisrtIndex==-1:
                fisrtIndex=i
                lastindex=fisrtIndex
            elif nums[i]==target and fisrtIndex>-1:
                lastindex=i
        return [fisrtIndex,lastindex]
