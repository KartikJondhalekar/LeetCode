class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]

        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            stone_x = -heapq.heappop(maxheap)
            stone_y = -heapq.heappop(maxheap)

            if stone_x == stone_y:
                continue
            else:
                heapq.heappush(maxheap, -abs(stone_x - stone_y))

        return -maxheap[0] if len(maxheap) > 0 else 0
