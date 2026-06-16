# Problem #215: Kth Largest Element in an Array
# Difficulty : Medium
# Language   : python3
# Runtime    : 91 ms
# Memory     : 30.9 MB
# URL        : https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]