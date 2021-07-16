'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
'''
def findDuplicate(self, nums: List[int]) -> int:
        '''return Counter(nums).most_common(1)[0][0]'''
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return i