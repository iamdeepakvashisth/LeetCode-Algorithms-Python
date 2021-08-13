'''
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

'''

def largeGroupPositions(self, s: str) -> List[List[int]]:
        res, ind = [], []
        for i in range(len(s)):
            if i == 0:
                sIndex, eIndex = 0, 0
            elif s[i] == s[i-1]:
                eIndex = i
                if i == len(s)-1:
                    res.append([sIndex, eIndex])
            else:
                res.append([sIndex, eIndex])
                sIndex = i
                eIndex = i     
                if i == len(s)-1:
                    res.append([sIndex, eIndex])
        for i in res:
            if i[1] - i[0] >= 2:
                ind.append(i)
        if len(ind) > 0:
            return ind 
        else:
            return []
        
        
                
                
            
        
        
        
