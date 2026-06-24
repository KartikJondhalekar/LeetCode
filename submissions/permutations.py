# Problem #46: Permutations
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.5 MB
# URL        : https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)

            perms = new_perms

        return perms