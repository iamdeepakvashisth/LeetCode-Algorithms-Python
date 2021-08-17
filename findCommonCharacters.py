'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.


'''


def commonChars(self, words: List[str]) -> List[str]:
        finalRes = []
        temp = 0
        for i in set(words[0]):
            res = []
            res.append(words[0].count(i))
            for j in range(1, len(words)):
                res.append(words[j].count(i))
            if min(res) > 0 :
                temp = min(res)
                while temp > 0:
                    finalRes.append(i)
                    temp -= 1
            else:
                pass
        return finalRes