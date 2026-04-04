# Problem #19: Remove Nth Node From End of List
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 17.6 MB
# URL        : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        prev = dummy
        
        for i in range(n):
            curr = curr.next

        while curr.next:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next