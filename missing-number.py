class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter=0
        nums.sort()
        print(nums)
        
        for n in nums:
            if counter == n:
                counter+=1
            else:
                return counter
        return counter
        