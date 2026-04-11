# Problem #84: Largest Rectangle in Histogram
# Difficulty : Hard
# Language   : python3
# Runtime    : 116 ms
# Memory     : 36.3 MB
# URL        : https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height_stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while height_stack and height_stack[-1][1] > h:
                index, height = height_stack.pop()
                max_area = max(height * (i - index), max_area)
                start = index
            height_stack.append((start, h))

        for i, h in height_stack:
            max_area = max(h * (len(heights) - i), max_area)

        return max_area
