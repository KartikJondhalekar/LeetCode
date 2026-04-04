# Problem #121: Best Time to Buy and Sell Stock
# Difficulty : Easy
# Language   : python3
# Runtime    : 71 ms
# Memory     : 27 MB
# URL        : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        buy = prices[0]
        
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
                
        return profit


        
            
        