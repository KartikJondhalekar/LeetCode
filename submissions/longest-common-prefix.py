# Problem #14: Longest Common Prefix
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.9 MB
# URL        : https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = len(strs[0])
        
        for s in strs:
            n = min(n, len(s))
            
        if n == 0:
            return res
        
        for i in range(n):
            c = ''
            for s in strs:
                if c == '':
                    c = s[i]
                elif s[i] == c:
                    continue
                else: 
                    c = ''
                    break
                    
            if c != '':
                res += c
            else:
                break
                
        return res
            