# Problem #152: Maximum Product Subarray
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 19.8 MB
# URL        : https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))

        return res