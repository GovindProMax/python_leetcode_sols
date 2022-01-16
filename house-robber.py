class Solution:
    def rob(self, nums: List[int]) -> int:
        firstrob=0
        secondrob=0
        
        for money in nums:
            temp=max(money+firstrob,secondrob)
            firstrob=secondrob
            secondrob=temp
        return secondrob