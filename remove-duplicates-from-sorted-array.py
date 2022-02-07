class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0,1
        for i in range(len(nums)-1):
            if nums[slow]!= nums[fast]:
                slow +=1
                nums[slow]= nums[fast]
                
                fast +=1
            else:
                fast+=1
        print(nums)
        return slow+1

## Alternate Soln

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mydict={}      
        for i,n in enumerate(nums):
            if n in mydict:
                nums[i] = '_'
            else:
                mydict[n]=0
        while '_' in nums: nums.remove('_')
        #return nums[-1]