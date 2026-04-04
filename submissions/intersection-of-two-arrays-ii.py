# Problem #350: Intersection of Two Arrays II
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.9 MB
# URL        : https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
    
        res = []
        i = j = 0
    
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return res