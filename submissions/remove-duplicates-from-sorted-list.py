# Problem #83: Remove Duplicates from Sorted List
# Difficulty : Easy
# Language   : python3
# Runtime    : 3 ms
# Memory     : 16.7 MB
# URL        : https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start from the head of the list
        current = head

        while current and current.next:
            # If the current value is the same as the next, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
