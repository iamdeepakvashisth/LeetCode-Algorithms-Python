#Find Lucky Integer in an Array
def findLucky(self, arr: List[int]) -> int:
        numDic={}
        largest =-1
        for i in arr:
            if i not in numDic:
                numDic[i]=1
            else:
                numDic[i]+=1
        for key, value in numDic.items():
            if key == value and key>largest:
                largest=key
        return largest
