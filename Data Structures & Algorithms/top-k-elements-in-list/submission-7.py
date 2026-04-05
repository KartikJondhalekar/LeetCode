class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        temp = []
        res = []

        for num, f in freq.items():
            heapq.heappush(temp, (f, num))
            if len(temp) > k:
                heapq.heappop(temp)

        while temp:
            res.append(heapq.heappop(temp)[1])
                
        return res