class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet= set(nums)
        maxLength=0
        for n in nums:
            if (n-1) not in numsSet:
                lengthTemp = 1
                
                while (n+lengthTemp) in numsSet:
                    lengthTemp+=1
                maxLength=max(maxLength,lengthTemp)
        
        return maxLength
        
        