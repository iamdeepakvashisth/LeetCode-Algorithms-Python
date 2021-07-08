'''
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.
'''

def checkZeroOnes(self, s: str) -> bool:
        lenO, lenZ = 0, 0
        listO = s.split('0')
        for i in listO:
            if i != '' and lenO < len(i):
                lenO = len(i)
        listZ = s.split('1')
        for i in listZ:
            if i != '' and lenZ < len(i):
                lenZ = len(i)
        return lenO > lenZ