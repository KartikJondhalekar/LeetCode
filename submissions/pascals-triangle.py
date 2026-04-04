# Problem #118: Pascal's Triangle
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            curr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(curr)

        return res