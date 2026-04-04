# Problem #26: Remove Duplicates from Sorted Array
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.8 MB
# URL        : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l, r = 0, 1
        
        while r < len(nums):
            if (nums[l] != nums[r]):
                l += 1
                nums[l] = nums[r]
                
            r += 1
            
        return l + 1