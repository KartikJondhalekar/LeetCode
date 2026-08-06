# Problem #57: Insert Interval
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 21.5 MB
# URL        : https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for start, end in intervals:
            if end < newInterval[0]:
                res.append([start, end])
            elif start > newInterval[1]:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        res.append(newInterval)

        return res