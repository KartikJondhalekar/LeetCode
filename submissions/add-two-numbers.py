# Problem #2: Add Two Numbers
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 18.1 MB
# URL        : https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        op = res
        carry = 0

        # while l1 and l2:
        #     res.next = ListNode((l1.val + l2.val + carry) % 10)
            
        #     if l1.val + l2.val + carry > 9:
        #         carry = 1
        #     else:
        #         carry = 0

        #     l1 = l1.next
        #     l2 = l2.next
        #     res = res.next

        # while l1:
        #     res.next = ListNode((l1.val + carry) % 10)
        #     if l1.val + carry > 9:
        #         carry = 1
        #     else:
        #         carry = 0

        #     l1 = l1.next
        #     res = res.next

        # while l2:
        #     res.next = ListNode((l2.val + carry) % 10)
        #     if l2.val + carry > 9:
        #         carry = 1
        #     else:
        #         carry = 0
        #     l2 = l2.next
        #     res = res.next

        # if carry == 1:
        #     res.next = ListNode(carry)

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            res.next = ListNode(total % 10)
            res = res.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return op.next