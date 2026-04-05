# Problem #347: Top K Frequent Elements
# Difficulty : Medium
# Language   : python3
# Runtime    : 11 ms
# Memory     : 24.9 MB
# URL        : https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Using Heap
        # freq = dict()

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # temp = []
        # res = []

        # for num, f in freq.items():
        #     heapq.heappush(temp, (f, num))
        #     if len(temp) > k:
        #         heapq.heappop(temp)

        # while temp:
        #     res.append(heapq.heappop(temp)[1])
                
        # return res

        # Using Bucket Sort

        freq = dict()

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, f in freq.items():
            buckets[f].append(num)

        res = []
        i = len(nums)

        while i > 0:
            while len(buckets[i]) != 0  and len(res) < k:
                res.append(buckets[i].pop())
            i -= 1
        return res