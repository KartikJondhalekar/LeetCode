# Problem #70: Climbing Stairs
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first = 1
        second = 2
        
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third
            
        return second
