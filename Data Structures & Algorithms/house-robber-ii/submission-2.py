class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo1 = [-1] * n
        memo2 = [-1] * n

        def dfs(i, end, memo):
            if i > end:
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(
                dfs(i + 1, end, memo),
                nums[i] + dfs(i + 2, end, memo)
            )

            return memo[i]

        return max(
            dfs(0, n - 2, memo1),  # Rob from house 0 to n-2
            dfs(1, n - 1, memo2)   # Rob from house 1 to n-1
        )