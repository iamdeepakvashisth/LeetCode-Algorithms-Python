 #217. Contains Duplicate
 #Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True