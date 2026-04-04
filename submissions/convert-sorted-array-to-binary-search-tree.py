# Problem #108: Convert Sorted Array to Binary Search Tree
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.2 MB
# URL        : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def addNodeToBST(start, end):             
            if start > end:
                return
                
            mid = (start + end) // 2
            
            node = TreeNode(nums[mid], addNodeToBST(start, mid - 1), addNodeToBST( mid + 1, end))            
            
            return node
            
        root = addNodeToBST(0, len(nums) - 1)            
                
        return root
            
            
        