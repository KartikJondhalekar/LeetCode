# Problem #90: Subsets II
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.5 MB
# URL        : https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            res.append(subset[::])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                subset.append(nums[j])
                backtrack(j + 1, subset)

                subset.pop()

        backtrack(0, [])

        return res