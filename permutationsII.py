'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in set(permutations(nums)):
            result.append(list(i))
        return result