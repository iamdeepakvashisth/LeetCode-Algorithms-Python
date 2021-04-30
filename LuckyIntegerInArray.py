#Find Lucky Integer in an Array
 def findLucky(self, arr: List[int]) -> int:
        numDic={}
        listOfLuckyNums=[-1]
        largest =-1
        for i in arr:
            if i not in numDic:
                numDic[i]=1
            else:
                numDic[i]+=1
        for key, value in numDic.items():
            if key == value:
                listOfLuckyNums.append(key)
        return max(listOfLuckyNums)
