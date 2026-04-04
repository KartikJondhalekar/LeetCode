# Problem #11: Container With Most Water
# Difficulty : Medium
# Language   : python3
# Runtime    : 106 ms
# Memory     : 28.4 MB
# URL        : https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        mostWater = 0
        left = 0
        right = len(height) - 1

        while left < right:
            currWater = (right - left) * min(height[left], height[right])
            mostWater = max(mostWater, currWater)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mostWater