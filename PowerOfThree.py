 #326. Power of three
 #Given an integer n, return true if it is a power of three. Otherwise, return false. An integer n is a power of three, if there exists an integer x such that n == 3x.
 def isPowerOfThree(self, n: int) -> bool:
        if n==0 or n==2 or n<0:
            return False
        x=log(n,3)
        return True if n==3**ceil(x) or n==3**floor(x) else False