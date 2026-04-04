# Problem #189: Rotate Array
# Difficulty : Medium
# Language   : python3
# Runtime    : 4 ms
# Memory     : 25.7 MB
# URL        : https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n               
        if k == 0:                  
            return
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1   
            
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        
    
                
                