# Problem #199: Binary Tree Right Side View
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 19.5 MB
# URL        : https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # #BFS
        # res = []
        # q = deque([root])

        # while q:
        #     rightMost = None
        #     qLen = len(q)

        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             rightMost = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightMost:
        #         res.append(rightMost.val)
        # return res

        # #DFS
        res = []

        def dfs(node, level):
            if not node:
                return None

            if level == len(res):
                res.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)

        return res

