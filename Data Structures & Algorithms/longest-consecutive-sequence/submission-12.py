class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n log n)
        # Space: O(n)
        # heap = []
        # res = 1
        # curr_max = 1 

        # if not nums:
        #     return 0

        # for num in nums:
        #     heapq.heappush(heap, num)

        # prev = heapq.heappop(heap)

        # while heap:
        #     curr = heapq.heappop(heap)
        #     diff = abs(curr - prev)
        #     if diff == 0:                
        #         continue
        #     if diff == 1:
        #         curr_max += 1
        #     else:
        #         curr_max = 1
        #     res = max(res, curr_max)
        #     prev = curr
        
        # return res 

        seq = set(nums)
        curr_max = res = 0

        for num in seq:
            if (num - 1) not in seq:
                curr_max = 1
                num += 1
                while (num) in seq:
                    curr_max += 1
                    num += 1
                res = max(res, curr_max)

        return res



