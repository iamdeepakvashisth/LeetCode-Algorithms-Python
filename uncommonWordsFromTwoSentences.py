'''
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

'''

def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list1 = s1.split()
        list2 = s2.split()
        res = []
        dictionary = {}
        for i in list1:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in list2:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        print(dictionary)
        for k, v in dictionary.items():
            if v == 1:
                res.append(k)
        return res
                