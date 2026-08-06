# Problem #45: Jump Game II
# Difficulty : Medium
# Language   : python3
# Runtime    : 4 ms
# Memory     : 20.1 MB
# URL        : https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0

            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res