# Problem #424: Longest Repeating Character Replacement
# Difficulty : Medium
# Language   : python3
# Runtime    : 75 ms
# Memory     : 19.5 MB
# URL        : https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = maxf = res = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxf = max(count[s[r]], maxf)

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res