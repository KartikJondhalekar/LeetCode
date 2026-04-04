# Problem #518: Coin Change II
# Difficulty : Medium
# Language   : python3
# Runtime    : 121 ms
# Memory     : 18.1 MB
# URL        : https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]