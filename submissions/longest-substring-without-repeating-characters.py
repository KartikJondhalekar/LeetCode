# Problem #3: Longest Substring Without Repeating Characters
# Difficulty : Medium
# Language   : python3
# Runtime    : 19 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r]) 
            res = max(r - l + 1, res)

        return res