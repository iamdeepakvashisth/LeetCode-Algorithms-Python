'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

'''

def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiou"
        count = 0
        for i in range(int(len(s)/2)):
            if s[i].lower() in vowels:
                count += 1
            if s[-1-i].lower() in vowels:
                count -= 1
        return count == 0
        