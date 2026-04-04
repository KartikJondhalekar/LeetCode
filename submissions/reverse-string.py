# Problem #344: Reverse String
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 23.1 MB
# URL        : https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            