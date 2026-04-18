# Problem #239: Sliding Window Maximum
# Difficulty : Hard
# Language   : python3
# Runtime    : 194 ms
# Memory     : 34.8 MB
# URL        : https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        dq = collections.deque()

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if (r + 1) >= k:
                res.append(nums[dq[0]])
                l += 1

            r += 1

        return res