# Problem #27: Remove Element
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 16.7 MB
# URL        : https://leetcode.com/problems/remove-element/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Points to the position for the next non-val element

        # Traverse through the list
        for i in range(len(nums)):
            # Only move non-val elements to the front
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # `k` is now the length of the array with all occurrences of `val` removed
        return k
