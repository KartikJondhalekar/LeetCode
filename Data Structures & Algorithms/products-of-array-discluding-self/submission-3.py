class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        n = len(nums)
        res = [1 for _ in range(n)]
        for i in range(n):
            for j, k in enumerate(nums):
                if i == j:
                    continue
                res[i] *= k
        return res

