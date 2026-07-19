# Problem #647: Palindromic Substrings
# Difficulty : Medium
# Language   : python3
# Runtime    : 139 ms
# Memory     : 19.4 MB
# URL        : https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l, r = i , i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l, r = i , i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
