class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = dict()

        for i, num in enumerate(nums):
            if (target - num) in ids:
                return [ids[target-num], i]
            
            ids[num] = i

