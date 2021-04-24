def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s=s+str(i)
        s2=str(int(s)+k)
        return [int(i) for i in s2]
        
"""
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""