# Problem #5: Longest Palindromic Substring
# Difficulty : Medium
# Language   : python3
# Runtime    : 315 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Bruteforce: Time: O(n^3) 
        # def isPalindrome(l, r):
        #     while l <= r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1

        #     return True

        # start, end = 0, len(s) - 1
        # res = ""

        # if len(s) < 2 or isPalindrome(start, end):
        #     return s

        # while start < len(s):
        #     while end >= start:
        #         print(s[start : end + 1])
        #         if isPalindrome(start, end) and len(s[start : end + 1]) > len(res):
        #             res = s[start : end + 1]            
        #         end -= 1
        #     end = len(s) - 1
        #     start += 1

        # return res

        #Time: O(n^2)

        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    if resLen > len(res):
                        res = s[l: r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    if resLen > len(res):
                        res = s[l: r + 1]
                l -= 1
                r += 1

        return res