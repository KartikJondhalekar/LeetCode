# Problem #384: Shuffle an Array
# Difficulty : Medium
# Language   : python3
# Runtime    : 36 ms
# Memory     : 21.8 MB
# URL        : https://leetcode.com/problems/shuffle-an-array/

class Solution:
    
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums[:]
        
        for i in range(len(nums) - 1, -1, -1):
            j = random.randint(0, i)
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()