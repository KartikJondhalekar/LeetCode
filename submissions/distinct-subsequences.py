# Problem #115: Distinct Subsequences
# Difficulty : Hard
# Language   : python3
# Runtime    : 415 ms
# Memory     : 42 MB
# URL        : https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        T = len(t)
        S = len(s)
        cache = [[-1]*(T+1) for _ in range(S+1)]
        def backtrack(i,j):
            if j==T:
                return 1
            if i==S:
                return 0
            if cache[i][j]!=-1:
                return cache[i][j]
            if s[i]==t[j]:
                cache[i][j] = backtrack(i+1,j+1) + backtrack(i+1,j)
            else:
                cache[i][j] = backtrack(i+1,j)
            return cache[i][j]
        return backtrack(0,0)