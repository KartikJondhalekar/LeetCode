class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Brute Force
        # n = len(nums)
        # res = [1 for _ in range(n)]
        # for i in range(n):
        #     for j, k in enumerate(nums):
        #         if i == j:
        #             continue
        #         res[i] *= k
        # return res

        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for j in range(len(nums) - 2, -1, -1):
            right *= nums[j + 1] 
            res[j] *= right

        return res


