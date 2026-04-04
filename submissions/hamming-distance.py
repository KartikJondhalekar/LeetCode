# Problem #461: Hamming Distance
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        
#         while x > 0 and y > 0:
#             if (x & 1) ^ (y & 1):
#                 res += 1
#             x = x >> 1
#             y = y >> 1
            
#         while x:
#             res += 1
#             x &= x - 1
            
#         while y:
#             res += 1
#             y &= y - 1
            
        xor = x ^ y
        
        while xor:
            xor &= xor - 1
            res += 1
                    
        return res