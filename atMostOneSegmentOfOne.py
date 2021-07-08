'''
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
'''
def checkOnesSegment(self, s: str) -> bool:
        count = 0
        strList = s.split('0')
        for i in strList:
            if i != '':
                count += 1 
        return count == 1