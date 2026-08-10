# Problem #1899: Merge Triplets to Form Target Triplet
# Difficulty : Medium
# Language   : python3
# Runtime    : 28 ms
# Memory     : 54 MB
# URL        : https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False] * 3

        for triplet in triplets:
            if (triplet[0] > target[0] or
               triplet[1] > target[1] or
               triplet[2] > target[2]):
               continue

            if triplet[0] == target[0]:
                found[0] = True
            
            if triplet[1] == target[1]:
                found[1] = True
            
            if triplet[2] == target[2]:
                found[2] = True

        return all(found)