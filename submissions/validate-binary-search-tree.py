# Problem #98: Validate Binary Search Tree
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.8 MB
# URL        : https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def validate(node, minVal = float('-inf'), maxVal = float('inf')) -> bool:
#             if not node:
#                 return True
            
#             val = node.val
            
#             if val <= minVal or val >= maxVal:
#                 return False
            
#             if not validate(node.right, val, maxVal):
#                 return False
            
#             if not validate(node.left, minVal, val):
#                 return False
            
#             return True
                
        
#         return validate(root)

        # Iterative approach
        stack = []
        prev = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            if root.val <= prev:
                return False
            
            prev = root.val
            
            root = root.right
            
        return True
            
        