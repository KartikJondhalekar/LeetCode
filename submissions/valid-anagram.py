# Problem #242: Valid Anagram
# Difficulty : Easy
# Language   : python3
# Runtime    : 12 ms
# Memory     : 18 MB
# URL        : https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            seen[t[i]] = seen.get(t[i], 0) - 1

        return all(count == 0 for count in seen.values())