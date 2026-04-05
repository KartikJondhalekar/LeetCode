class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []

        while k > 0:
            most_freq = None
            max_freq = 0
            for num, f in freq.items():
                if f > max_freq:
                    max_freq = f
                    most_freq = num
            res.append(most_freq)
            freq[most_freq] = 0
            k -= 1    

        return res
                