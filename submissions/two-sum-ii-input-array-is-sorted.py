# Problem #167: Two Sum II - Input Array Is Sorted
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 20.7 MB
# URL        : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]

            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1]

        