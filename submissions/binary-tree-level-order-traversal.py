# Problem #102: Binary Tree Level Order Traversal
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 18.7 MB
# URL        : https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
        
#         def dfs(node, level):
#             if not node:
#                 return
            
#             if level == len(res):
#                 res.append([])
                
            
#             res[level].append(node.val)
            
#             dfs(node.left, level + 1)
#             dfs(node.right, level + 1)
            
#         dfs(root, 0)
        
#         return res

        # Iterative Approach
        if not root:
            return []
        
        queue = deque([root])
        res = []
        
        while queue:
            level_range = len(queue)
            level = []
            
            for _ in range(level_range):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(level)
            
        return res