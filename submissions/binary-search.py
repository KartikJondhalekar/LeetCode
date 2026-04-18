# Problem #704: Binary Search
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 20.5 MB
# URL        : https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1