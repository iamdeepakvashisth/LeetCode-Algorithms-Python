'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

'''

def sortedSquares(self, nums: List[int]) -> List[int]:
    sqNums = [i*i for i in nums]
    return sorted(sqNums)