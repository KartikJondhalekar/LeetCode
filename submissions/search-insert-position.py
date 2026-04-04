# Problem #35: Search Insert Position
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.4 MB
# URL        : https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # When the loop ends, left is the correct insertion point
        return left
