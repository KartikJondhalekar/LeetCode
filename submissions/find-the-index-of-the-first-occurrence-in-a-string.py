# Problem #28: Find the Index of the First Occurrence in a String
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.9 MB
# URL        : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if i + len(needle) > len(haystack):
                break
            elif haystack[i : i +len(needle)] == needle:
                return i                
        
        return -1
        