# Problem #122: Best Time to Buy and Sell Stock II
# Difficulty : Medium
# Language   : python3
# Runtime    : 4 ms
# Memory     : 19 MB
# URL        : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l , r = 0, 1
        p = 0
        
        while r < len(prices):
            if (prices[l] < prices[r]):
                p += prices[r] - prices[l]
            
            l += 1
            r += 1
                
        return p
        