# Problem #326: Power of Three
# Difficulty : Easy
# Language   : python3
# Runtime    : 11 ms
# Memory     : 17.9 MB
# URL        : https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        log_val = math.log(n, 3)
        return abs(round(log_val) - log_val) < 1e-10
        
#         if n <= 0:
#             return False
        
#         while n % 3 == 0:
#             n = n // 3
            
#         return n == 1