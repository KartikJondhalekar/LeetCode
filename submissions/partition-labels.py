# Problem #763: Partition Labels
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 19.4 MB
# URL        : https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = 0
        start = end = 0

        for i, c in enumerate(s):
            size += 1

            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res