# Problem #268: Missing Number
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.9 MB
# URL        : https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = n * (n + 1) // 2
        
        for num in nums:
            res -= num
            
        return res