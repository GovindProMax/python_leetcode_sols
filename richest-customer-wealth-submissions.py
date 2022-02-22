class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        r=len(accounts)
        c=len(accounts[0])
        maxTotal, currSum = 0, 0
        
        for row in range(0,r):
            for column in range(0,c):
                currSum = currSum + accounts[row][column]
            maxTotal=max(maxTotal,currSum)
            currSum=0
        
        return maxTotal