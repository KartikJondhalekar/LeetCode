# Problem #69: Sqrt(x)
# Difficulty : Easy
# Language   : python3
# Runtime    : 3 ms
# Memory     : 16.6 MB
# URL        : https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
