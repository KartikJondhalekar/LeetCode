# Problem #746: Min Cost Climbing Stairs
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.3 MB
# URL        : https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])