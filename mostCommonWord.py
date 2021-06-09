def mostCommonWord(self, p: str, banned: List[str]) -> str:
        d={}
        import re
        s = re.sub("[!?',;.]+", ' ',p).lower()
        l=s.split()
        for i in l:
            if i not in banned and i not in d:
                d[i]=1
            elif i not in banned: 
                d[i]+=1
        return max(d, key=d.get)
