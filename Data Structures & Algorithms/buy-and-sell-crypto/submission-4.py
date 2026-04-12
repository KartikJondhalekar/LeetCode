class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        buy_price = prices[l]

        while r < len(prices):
            curr_price = prices[r]

            profit = max(profit, curr_price - buy_price)

            if curr_price < buy_price:
                buy_price = curr_price

            r += 1    
            
        return profit
            