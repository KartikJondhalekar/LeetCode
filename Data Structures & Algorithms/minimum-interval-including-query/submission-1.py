from heapq import heappush, heappop

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        heap = []         
        ans = [-1] * len(queries)

        i = 0

        for q, idx in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heappush(heap, (end - start + 1, end))
                i += 1

            while heap and heap[0][1] < q:
                heappop(heap)

            if heap:
                ans[idx] = heap[0][0]

        return ans