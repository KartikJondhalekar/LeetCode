# Problem #703: Kth Largest Element in a Stream
# Difficulty : Easy
# Language   : python3
# Runtime    : 9 ms
# Memory     : 25.3 MB
# URL        : https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
                    
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)