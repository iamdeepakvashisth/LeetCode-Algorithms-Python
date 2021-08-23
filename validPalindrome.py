'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

def isPalindrome(self, s: str) -> bool:
        newS = ''.join(i for i in s.lower() if i.isalnum())
        return newS == newS[::-1]