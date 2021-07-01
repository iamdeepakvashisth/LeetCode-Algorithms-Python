'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

'''

def findDuplicates(self, nums: List[int]) -> List[int]:
        dictionaryy = {}
        res = []
        for i in nums:
            if i not in dictionaryy:
                dictionaryy[i] = 1
            else:
                dictionaryy[i] += 1
        for key, value in dictionaryy.items():
            if value == 2:
                res.append(key)
        return res