class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            sell = prices[i]
            for j in range(i+1, len(prices)):
                buy = prices[j]
                profit = max(profit, buy - sell)
        return profit    
