class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            target = -sorted_nums[i]
            l, r = i + 1, n - 1

            while l < r:
                s = sorted_nums[l] + sorted_nums[r]

                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    r -= 1
                    l += 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1
                    
        return res