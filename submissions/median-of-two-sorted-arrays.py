# Problem #4: Median of Two Sorted Arrays
# Difficulty : Hard
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.3 MB
# URL        : https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ### Time: O(n + m)  Space: O(n + m)
        # res = []
        # med = 0
        # n, m = len(nums1), len(nums2)
        # i = j = 0

        # while i < n and j < m:
        #     if nums1[i] < nums2[j]:
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1

        # while i < n:
        #     res.append(nums1[i])
        #     i += 1

        # while j < m:
        #     res.append(nums2[j])
        #     j += 1

        # k = len(res)

        # if k % 2 == 0:
        #     med = (res[k // 2] + res[(k // 2) - 1]) / 2
        # else:
        #     med = res[k // 2]

        # return med

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            if Aleft > Bright:
                r -= 1

            if Bleft > Aright:
                l += 1