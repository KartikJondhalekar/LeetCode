# Problem #283: Move Zeroes
# Difficulty : Easy
# Language   : python3
# Runtime    : 4 ms
# Memory     : 18.6 MB
# URL        : https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
                
        for j in range(i, len(nums)):
            nums[j] = 0
            