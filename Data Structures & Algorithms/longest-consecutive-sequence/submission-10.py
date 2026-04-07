class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = []
        res = 1
        curr_max = 1 

        if not nums:
            return 0

        for num in nums:
            heapq.heappush(heap, num)

        prev = heapq.heappop(heap)

        while heap:
            curr = heapq.heappop(heap)
            diff = abs(curr - prev)
            if diff == 0:                
                continue
            if diff == 1:
                curr_max += 1
            else:
                curr_max = 1
            res = max(res, curr_max)
            prev = curr
        

        return res 