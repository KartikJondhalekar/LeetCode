# Problem #100: Same Tree
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 16.6 MB
# URL        : https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # If both nodes are None, they are the same
            if not p and not q:
                return True
            # If one of them is None or their values differ, they are not the same
            if not p or not q or p.val != q.val:
                return False

            # Recursively check the left and right subtrees
            return check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)
