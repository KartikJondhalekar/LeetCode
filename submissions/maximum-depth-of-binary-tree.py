# Problem #104: Maximum Depth of Binary Tree
# Difficulty : Easy
# Language   : python3
# Runtime    : 3 ms
# Memory     : 19 MB
# URL        : https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
         # Recursive DFS
#         if not root:
#             return 0
        
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
        
#         return 1 + max(left, right)

        # Iterative DFS
#         stack = [[root, 1]]
#         res = 0
        
#         while stack:
#             node, depth = stack.pop()
            
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
                
#         return res

        # Iterative BFS
        if not root:
            return 0
        
        q = deque([root])
        level = 0
        
        while q:            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level += 1
                
        return level