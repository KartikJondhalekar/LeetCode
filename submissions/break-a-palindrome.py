# Problem #1328: Break a Palindrome
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.6 MB
# URL        : https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if (len(palindrome) <= 1):
            return ""
        
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[0: i] + 'a' + palindrome[i + 1:]

        return palindrome[:-1] + 'b'