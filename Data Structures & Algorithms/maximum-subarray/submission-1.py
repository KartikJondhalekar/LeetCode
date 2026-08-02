class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = currSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > currSum + nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]

            res = max(res, currSum)

        return res