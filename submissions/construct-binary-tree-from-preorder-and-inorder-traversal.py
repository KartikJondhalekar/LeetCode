# Problem #105: Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 21.1 MB
# URL        : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## DFS - Time O(n**2)
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root

        ## DFS + HashMap
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None

            rootVal = preorder[self.preIdx]
            self.preIdx += 1

            root = TreeNode(rootVal)
            mid = indices[rootVal]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
