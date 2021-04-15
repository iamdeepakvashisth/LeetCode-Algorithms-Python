 258. Add Digits
 #Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
 def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum( int(numStr) for numStr in list(str(num)))
        return num