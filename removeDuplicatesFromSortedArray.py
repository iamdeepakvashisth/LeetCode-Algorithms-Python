def removeDuplicates(self, nums: List[int]) -> int:
        counter=0;
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[counter]!=nums[i]:
                counter+=1
                nums[counter]=nums[i]
        return counter+1
