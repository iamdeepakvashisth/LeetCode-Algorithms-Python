def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(map(ord, s)))==sorted(list(map(ord, t)))
        
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""