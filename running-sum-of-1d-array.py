class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp=0
        for index,val in enumerate(nums):
            temp=temp+nums[index]
            nums[index] =temp
            
            print(val,temp)
        return nums