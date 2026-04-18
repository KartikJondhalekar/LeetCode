# Problem #875: Koko Eating Bananas
# Difficulty : Medium
# Language   : python3
# Runtime    : 171 ms
# Memory     : 20.6 MB
# URL        : https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res