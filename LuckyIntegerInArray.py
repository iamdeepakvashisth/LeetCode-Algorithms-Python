#Find Lucky Integer in an Array
def findLucky(self, arr: List[int]) -> int:
        largest=-1
        for i in arr:
            if i==arr.count(i):
                if i>largest:
                    largest=i
        return largest