# Problem #101: Symmetric Tree
# Difficulty : Easy
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.8 MB
# URL        : https://leetcode.com/problems/symmetric-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]):
#             if not left and not right:
#                 return True
#             elif not left or not right or left.val != right.val:
#                 return False
#             else:
#                 return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            
#         return isMirror(root.left, root.right) if root else True

        #Iterative approach
        if not root:
            return True
        
        queue = deque()
        queue.append((root.left, root.right))
        
        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue
            elif not left or not right or left.val != right.val:
                return False
            
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
            
        return True
            
            
        
                
            
            
            