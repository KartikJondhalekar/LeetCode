# Problem #1046: Last Stone Weight
# Difficulty : Easy
# Language   : python3
# Runtime    : 1 ms
# Memory     : 19.5 MB
# URL        : https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)

            if stone_2 > stone_1:
                heapq.heappush(stones, (stone_1 - stone_2))

        stones.append(0)

        return abs(stones[0])