# Problem #217: Contains Duplicate
# Difficulty : Easy
# Language   : python3
# Runtime    : 7 ms
# Memory     : 32.2 MB
# URL        : https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)

        return False