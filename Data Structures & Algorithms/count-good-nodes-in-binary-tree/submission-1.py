# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, root.val)])
        res = 0

        while q:
            node, pathMax = q.popleft()

            if node.val >= pathMax:
                res += 1

            pathMax = max(pathMax, node.val)

            if node.left:
                q.append((node.left, pathMax))
            
            if node.right:
                q.append((node.right, pathMax))

        return res
