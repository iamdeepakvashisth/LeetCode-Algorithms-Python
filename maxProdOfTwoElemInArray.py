def maxProduct(self, nums: List[int]) -> int:
        sortlist=sorted(nums, reverse=True)
        return ((sortlist[0])-1)*((sortlist[1])-1)