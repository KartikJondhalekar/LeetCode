# Problem #278: First Bad Version
# Difficulty : Easy
# Language   : python3
# Runtime    : 36 ms
# Memory     : 17.6 MB
# URL        : https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1    
            else:
                start = mid + 1
            
        return start