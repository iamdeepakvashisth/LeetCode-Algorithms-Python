'''
Occurrences After Bigram
Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".
'''

def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        sText = text.split(" ")
        for i in range(len(sText)):
            if i+2 < len(sText) and sText[i] == first:
                if sText[i+1] == second:
                    res.append(sText[i+2])
        return res
                    
