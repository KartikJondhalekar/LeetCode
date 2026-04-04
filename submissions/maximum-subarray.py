# Problem #53: Maximum Subarray
# Difficulty : Medium
# Language   : python3
# Runtime    : 87 ms
# Memory     : 32 MB
# URL        : https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum