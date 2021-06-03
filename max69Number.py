'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

'''

def maximum69Number (self, num: int) -> int:
    s = str(num)
    for i in range(len(s)):
        if s[i] == "6":
            new_str=s.replace("6", "9",1)
            return int(new_str)
    return int(s)