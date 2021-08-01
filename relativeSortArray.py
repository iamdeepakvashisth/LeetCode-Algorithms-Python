'''
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

'''

def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        extra = sorted(set(arr1)-set(arr2))
        count = Counter(arr1)
        for i in arr2:
            res.extend([i]*count[i])
        for i in extra:
            res.extend([i]*count[i])
        return res
