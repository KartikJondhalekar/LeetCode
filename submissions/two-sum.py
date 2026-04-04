# Problem #1: Two Sum
# Difficulty : Easy
# Language   : python3
# Runtime    : 3 ms
# Memory     : 18.8 MB
# URL        : https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for ind, num in enumerate(nums):
            if (target - num) in pairs:
                return [pairs[target - num], ind]
            else:
                pairs[num] = ind

        return
