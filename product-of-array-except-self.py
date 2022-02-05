## Solution with division. My dumbass should read the whole question before answering. Worked well thoug
## Almost 99% better than other submissions

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=1
        ## Returnable List
        newlist=[]
        ## Check if a '0' is present
        isPresent=False
        ## Store number of 0s in the array
        n0=0
        for n in nums:
            if n!=0:
                result = result * n
            else:
                isPresent=True
                ##update number of 0s
                n0+=1
        for n in nums:
            ## If no 0 present
            if n!=0 and isPresent == False:
                newlist.append(int(result/n))
            ## If only 1 zero present
            elif n==0 and isPresent == True and n0==1:
                newlist.append(int(result/1))
            ## If more than one zero present
            else:
                newlist.append(0)
        return newlist

## Other solution without division. Not m solution but its neat so keepiing it for my reference.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *=nums[i]
        print(res)
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res