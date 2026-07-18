# Problem #213: House Robber II
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.4 MB
# URL        : https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],
                   self.helper(nums[:-1]),
                   self.helper(nums[1:]))

    def helper(self, nums:List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return max(rob1, rob2)