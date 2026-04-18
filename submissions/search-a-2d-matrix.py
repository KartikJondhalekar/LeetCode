# Problem #74: Search a 2D Matrix
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.3 MB
# URL        : https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## )(m * logn)
        # def binary_search(arr: List[int], target) -> int:
        #     l, r = 0, len(arr) - 1

        #     while l <= r:
        #         mid = (l + r) // 2

        #         if arr[mid] > target:
        #             r = mid - 1
        #         elif arr[mid] < target:
        #             l = mid + 1
        #         else:
        #             return mid

        #     return -1

        # for row in matrix:
        #     if row[-1] >= target:
        #         return binary_search(row, target) != -1

        # return False

        ##O(log(m * n))
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
