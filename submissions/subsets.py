# Problem #78: Subsets
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.4 MB
# URL        : https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [subset + [num] for subset in res]

        return res