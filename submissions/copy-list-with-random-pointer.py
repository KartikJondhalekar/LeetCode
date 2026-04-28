# Problem #138: Copy List with Random Pointer
# Difficulty : Medium
# Language   : python3
# Runtime    : 43 ms
# Memory     : 20 MB
# URL        : https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = { None : None }

        curr = head
        while curr:
            res[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = res[curr]
            copy.next = res[curr.next]
            copy.random = res[curr.random]
            curr = curr.next

        return res[head]