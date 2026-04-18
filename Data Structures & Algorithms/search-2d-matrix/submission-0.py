class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(arr: List[int], target) -> int:
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = (l + r) // 2

                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return mid

            return -1

        for row in matrix:
            if row[-1] >= target:
                return binary_search(row, target) != -1

        return False