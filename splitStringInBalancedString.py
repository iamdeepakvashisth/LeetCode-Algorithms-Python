'''
Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

'''

def balancedStringSplit(self, s: str) -> int:
        countR, countL, resCount = 0, 0, 0
        for i in s:
            if i == 'R':
                countR += 1
            else:
                countL += 1
            if countR == countL:
                resCount += 1
        return resCount