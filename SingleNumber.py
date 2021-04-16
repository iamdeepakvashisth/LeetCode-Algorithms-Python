#136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i)==1:
                return i