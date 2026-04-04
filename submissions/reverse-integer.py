# Problem #7: Reverse Integer
# Difficulty : Medium
# Language   : python3
# Runtime    : 35 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        # res = 0
        # neg = False if x >= 0 else True
        # x = -x if neg else x

        # while x > 0:
        #     if x % 10:
        #         res += x % 10
            
        #     x = x // 10
            
        #     if x > 0:
        #         if (-(res * 10) < -(2**31) and neg) or (((res * 10) > (2**31) - 1) and not neg):
        #             return 0
        #         res *= 10
            
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        res = 0
        neg = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow BEFORE multiplying
            if res > (INT_MAX - digit) // 10:
                return 0
            
            res = res * 10 + digit

        return -res if neg else res