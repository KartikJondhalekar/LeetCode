# Problem #665: Non-decreasing Array
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 20.5 MB
# URL        : https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue

            if changed:
                return False

            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]

            changed = True

        return True