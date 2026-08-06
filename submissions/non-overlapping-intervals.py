# Problem #435: Non-overlapping Intervals
# Difficulty : Medium
# Language   : python3
# Runtime    : 63 ms
# Memory     : 49.2 MB
# URL        : https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd:
                res += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end

        return res