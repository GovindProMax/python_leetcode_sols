class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mydict={}
        maxNum=nums[0]
        minNum=nums[0]
        for n in nums:
            if n > 0:
                if n > maxNum:
                    maxNum=n
                if n < minNum:
                    minNum=n
                mydict[n]=0
        number=1
        while(True):
            if (number in mydict):
                number=number+1
            else:
                return number