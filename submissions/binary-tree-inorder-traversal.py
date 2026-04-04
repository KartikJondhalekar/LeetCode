# Problem #94: Binary Tree Inorder Traversal
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 16.6 MB
# URL        : https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left

            # Current must be None at this point, so we pop the last element
            current = stack.pop()
            result.append(current.val)  # Visit the node

            # Move to the right subtree
            current = current.right

        return result