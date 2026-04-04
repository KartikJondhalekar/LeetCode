# Problem #190: Reverse Bits
# Difficulty : Easy
# Language   : python3
# Runtime    : 43 ms
# Memory     : 17.6 MB
# URL        : https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
#         bits = []
        
#         for i in range(32):
#             if n & 1:
#                 bits.append(1)
#             else:
#                 bits.append(0)
#             n >>= 1
            
#         for i in range(32):
#             if bits[i]:
#                 res += 2**(31 - i) 

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
                
        return res