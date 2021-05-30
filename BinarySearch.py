def search(self, nums: List[int], target: int) -> int:
        f, l = 0, len(nums)-1
        while f <= l:
            m = (f + l)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                l = m-1
            else:
                f = m + 1 
        return -1
