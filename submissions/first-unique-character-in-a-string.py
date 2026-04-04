# Problem #387: First Unique Character in a String
# Difficulty : Easy
# Language   : python3
# Runtime    : 97 ms
# Memory     : 18 MB
# URL        : https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        
        for c in s:
            if c not in seen.keys():
                seen[c] = 1
            else:
                seen[c] += 1
            
                
        for i, c in enumerate(s):
            if seen[c] == 1:
                return i
            
        return -1
            
            