'''
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 
'''

def removeDuplicates(self, s: str) -> str:
        li = []
        for i in s:
            if len(li) != 0 and li[-1] == i:
                li.pop()
            else:
                li.append(i)
        return "".join(li)