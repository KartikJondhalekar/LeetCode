# Problem #16: 3Sum Closest
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 17.7 MB
# URL        : https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minsum = sum(nums[:3])
        if target < minsum:
            return minsum
        maxsum = sum(nums[-3:])
        if target > maxsum:
            return maxsum
        print(nums)
        
        reverse = False
        if abs(maxsum - target) < abs(minsum - target):
            nums.reverse()
            reverse = True
        
        diff = float('inf')
        for c in range(len(nums)-2):
            a, b = c+1, len(nums)-1
            while a < b:
                res = target - (nums[a] + nums[b] + nums[c])
                if abs(res) < abs(diff):
                    diff = res
                if res == 0:
                    return target
                elif (not reverse and res > 0) or (reverse and res < 0):
                    a += 1
                else:
                    b -= 1
        return target - diff