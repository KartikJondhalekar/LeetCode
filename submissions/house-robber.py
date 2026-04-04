# Problem #198: House Robber
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2