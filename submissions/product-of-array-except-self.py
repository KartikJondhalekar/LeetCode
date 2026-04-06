# Problem #238: Product of Array Except Self
# Difficulty : Medium
# Language   : python3
# Runtime    : 35 ms
# Memory     : 25.1 MB
# URL        : https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]

        # # Brute Force
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         res[i] *= nums[j]         

        # return res

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1] 

        right = 1
        
        for j in range(n - 2, -1, -1):
            right *= nums[j + 1]
            res[j] *= right

        return res