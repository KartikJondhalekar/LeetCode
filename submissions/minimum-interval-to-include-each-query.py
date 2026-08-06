# Problem #1851: Minimum Interval to Include Each Query
# Difficulty : Hard
# Language   : python3
# Runtime    : 318 ms
# Memory     : 64.1 MB
# URL        : https://leetcode.com/problems/minimum-interval-to-include-each-query/

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        heap = []
        res = [-1] * len(queries)

        i = 0

        for q, idx in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heappush(heap, (end - start + 1, end))
                i += 1

            while heap and heap[0][1] < q:
                heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res