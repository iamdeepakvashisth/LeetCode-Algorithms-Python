def maxProductDifference(self, nums: List[int]) -> int:
        sortedNums=sorted(nums, reverse = True)
        return (sortedNums[0]*sortedNums[1]) - (sortedNums[-2] * sortedNums[-1])
      