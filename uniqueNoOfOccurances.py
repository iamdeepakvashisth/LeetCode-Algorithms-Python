'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
'''

def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return len(d) == len(set(d.values()))
        