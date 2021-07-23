'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in list(permutations(nums)):
            result.append(list(i))
        return result
            
