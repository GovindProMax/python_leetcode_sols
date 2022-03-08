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
        
## Better Solution ##
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        idealArr=n*(n+1)/2
        mysum=0
        for num in nums:
            mysum=mysum+num
        return int(idealArr - mysum)