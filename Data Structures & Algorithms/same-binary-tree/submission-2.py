# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True

        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False

        # stack = [(p, q)]

        # while stack:
        #     node1, node2 = stack.pop()

        #     if not node1 and not node2:
        #         continue
            
        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False

        #     stack.append((node1.left, node2.left))
        #     stack.append((node1.right, node2.right))

        # return True

        ## BFS
        queueP = [p]
        queueQ = [q]

        while queueP and queueQ:
            for _ in range(len(queueP)):
                nodeP = queueP.pop()
                nodeQ = queueQ.pop()

                if nodeP is None and nodeQ is None:
                    continue

                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                queueP.append(nodeP.left)
                queueP.append(nodeP.right)
                queueQ.append(nodeQ.left)
                queueQ.append(nodeQ.right)

        return True