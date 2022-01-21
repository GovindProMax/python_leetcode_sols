class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0
        while n > 0:
            if n&1:
                ans=ans+1
            n=n>>1
        
        return ans
### Alternate easy to understand ###
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            count += n % 2
            n = n >> 1
        
        return count    