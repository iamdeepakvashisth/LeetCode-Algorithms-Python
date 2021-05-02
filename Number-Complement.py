def findComplement(self, num: int) -> int:
        listOfBinary=[]
        str=""
        numToBinary='{0:0b}'.format(num)
        for i in numToBinary:
            if i =='0':
                listOfBinary.append('1')
            if i =='1':
                listOfBinary.append('0')
        listToString=str.join(listOfBinary) 
        return int(listToString, 2) #binary to decimal