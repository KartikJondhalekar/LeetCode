class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        memo1 = [-1] * (len(nums) - 1)
        memo2 = [-1] * (len(nums) - 1)

        arr1 = nums[0:-1]
        arr2 = nums[1:]

        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dfs(i + 1, arr, memo), arr[i] + dfs(i + 2, arr, memo))

            return memo[i]

        return max(dfs(0, arr1, memo1), dfs(0, arr2, memo2))