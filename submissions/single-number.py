# Problem #136: Single Number
# Difficulty : Easy
# Language   : python3
# Runtime    : 4 ms
# Memory     : 19.6 MB
# URL        : https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res