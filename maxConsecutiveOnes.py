'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

'''
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes, countOnes = 0, 0
        for i in nums:
            if i == 1:
                countOnes += 1
                if countOnes > maxOnes:
                    maxOnes = countOnes
            else:
                countOnes = 0
        return maxOnes