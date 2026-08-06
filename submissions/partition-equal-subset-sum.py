# Problem #416: Partition Equal Subset Sum
# Difficulty : Medium
# Language   : python3
# Runtime    : 647 ms
# Memory     : 19.2 MB
# URL        : https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]