class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l = height[0]
        max_r = height[-1]
        water = 0

        while l < r:
            if max_l <= max_r:
                l += 1
                if max_l - height[l] > 0:
                    water += max_l - height[l]
                else:
                    max_l = height[l]
            else:
                r -= 1
                if max_r - height[r] > 0:
                    water += max_r - height[r]
                else:
                    max_r = height[r]

        return water