# Problem #973: K Closest Points to Origin
# Difficulty : Medium
# Language   : python3
# Runtime    : 95 ms
# Memory     : 24.9 MB
# URL        : https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max Heap
        maxHeap = []

        for x, y in points:
            dist = - ((x ** 2) + (y ** 2))
            heapq.heappush(maxHeap, [dist, x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])

        return res