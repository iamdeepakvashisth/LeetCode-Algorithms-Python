def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        summ=1
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                summ+=i
                summ+=num//i
        return summ==num