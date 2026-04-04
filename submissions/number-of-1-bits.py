# Problem #191: Number of 1 Bits
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        
        # while n > 0:
        #     if n & 1:
        #         bits += 1
        #     n = n >> 1
        
        while n:
            n &= n - 1
            bits += 1
            
        return bits