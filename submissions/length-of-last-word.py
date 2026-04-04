# Problem #58: Length of Last Word
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 16.7 MB
# URL        : https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces and split the string by spaces
        words = s.strip().split(" ")
        
        # Return the length of the last word
        return len(words[-1])
