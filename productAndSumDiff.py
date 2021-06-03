'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
'''

def subtractProductAndSum(self, n: int) -> int:
    p,s=1,0
    for i in str(n):
        p=p*int(i)
        s=s+int(i)
    return p-s