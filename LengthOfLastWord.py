def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
        
"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""