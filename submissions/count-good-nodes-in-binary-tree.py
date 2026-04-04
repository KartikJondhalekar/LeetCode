# Problem #1448: Count Good Nodes in Binary Tree
# Difficulty : Medium
# Language   : python3
# Runtime    : 131 ms
# Memory     : 32.1 MB
# URL        : https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def checkNode(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                return 1 + checkNode(node.left, node.val) + checkNode(node.right, node.val)
            else:
                return checkNode(node.left, maxVal) + checkNode(node.right, maxVal)
            

        return checkNode(root, root.val)