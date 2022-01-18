class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        my_dict={}

        buy_price=prices.pop(0)
        max_profit=0
        
        print(my_dict)
        
        for n in range(0,len(prices)):
            
            current_profit = max(prices) - buy_price
            buy_price=prices.pop(0)  
            max_profit=max(current_profit,max_profit)
        
        return max_profit

 ### Optimal Solution ###

 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        
        maxProfit=0
        
        while right < len(prices):
            if prices[left] < prices [right]:
                currProfit = prices[right] - prices [left]
                maxProfit = max (maxProfit, currProfit)
            else:
                left=right
            right+=1
        
        return (maxProfit)
        