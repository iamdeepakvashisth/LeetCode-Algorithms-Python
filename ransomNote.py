'''
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

'''

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteLi = Counter(ransomNote)
        magazineLi = Counter(magazine)
        for i in ransomNote:
            if i in magazineLi and ransomNoteLi[i] <= magazineLi[i]:
                    pass
            else:
                return False
        return True   