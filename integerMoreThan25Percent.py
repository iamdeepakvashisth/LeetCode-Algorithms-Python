'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 
'''
def findSpecialInteger(self, arr: List[int]) -> int:
        dictionry = {}
        percent = len(arr)/4
        for i in arr:
            if i not in dictionry:
                dictionry[i] = 1
            else:
                dictionry[i] += 1
        for key, value in dictionry.items():
            if value > percent:
                return key
        