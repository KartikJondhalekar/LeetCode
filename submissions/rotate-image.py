# Problem #48: Rotate Image
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):  # Only loop where j > i
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for ind, row in enumerate(matrix):
            matrix[ind] = row[: : -1]
            