# Problem #15: 3Sum
# Difficulty : Medium
# Language   : python3
# Runtime    : 559 ms
# Memory     : 20.7 MB
# URL        : https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
                
            l, r = i + 1, n - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res