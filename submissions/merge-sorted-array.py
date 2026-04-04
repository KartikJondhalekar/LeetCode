# Problem #88: Merge Sorted Array
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18 MB
# URL        : https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m + n - 1
        i, j = m - 1, n - 1
                
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[l] = nums1[i]
                i -= 1
            else:
                nums1[l] = nums2[j]
                j -= 1
                    
            l -= 1
            
                    
        while i >= 0:
            nums1[l] = nums1[i]
            i -= 1
            l -= 1
                
        while j >= 0:
            nums1[l] = nums2[j]
            j -= 1
            l -= 1
    
    
