'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 
'''

def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr=""
        word1Len = len(word1)
        word2Len = len(word2)
        firstHalf, secondhalf ="", ""
        if word1Len < word2Len:
            firstHalf = word2[:len(word1)]
            secondhalf = word2[len(word1):]
        else:
            firstHalf = word1[:len(word2)]
            secondhalf = word1[len(word2):]
        for i in range(len(firstHalf)):
            newStr= newStr+(word1[i]+word2[i])
        newStr += secondhalf
        return newStr