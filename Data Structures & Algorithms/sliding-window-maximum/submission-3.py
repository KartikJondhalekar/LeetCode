class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        i = 0

        while i + k <= len(nums):
            prev_max = float('-inf')
            prev_max = max(max(nums[i: i + k]), prev_max)
            res.append(prev_max)
            i += 1

        return res
