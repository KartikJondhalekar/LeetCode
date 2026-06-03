# Problem #235: Lowest Common Ancestor of a Binary Search Tree
# Difficulty : Medium
# Language   : python3
# Runtime    : 57 ms
# Memory     : 22.6 MB
# URL        : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # while root:
        #     if p.val < root.val and q.val < root.val:
        #         root = root.left
        #     elif p.val > root.val and q.val > root.val:
        #         root = root.right
        #     else:
        #         return root

        if not root or not p or not q:
            return None

        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


            