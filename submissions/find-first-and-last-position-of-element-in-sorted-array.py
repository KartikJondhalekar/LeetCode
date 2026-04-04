# Problem #34: Find First and Last Position of Element in Sorted Array
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.8 MB
# URL        : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target, findFirst):
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    result = mid  # Store the found index
                    if findFirst:
                        right = mid - 1  # Search left for first occurrence
                    else:
                        left = mid + 1   # Search right for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        first = binarySearch(nums, target, True)
        last = binarySearch(nums, target, False)

        return [first, last]