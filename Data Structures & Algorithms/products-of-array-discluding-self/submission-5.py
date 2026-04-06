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

        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]
        n = len(nums) - 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]


        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]

        return list(prefix[i] * suffix[i] for i in range(len(nums)))


