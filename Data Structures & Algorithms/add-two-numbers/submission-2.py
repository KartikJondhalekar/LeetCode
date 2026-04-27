# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        carry = 0

        while l1 and l2:
            addition = (l1.val + l2.val) 
            res.next =  ListNode(addition % 10 + carry)

            carry = 1 if addition > 9 else 0

            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            addition = (l1.val + carry) 
            res.next =  ListNode(addition % 10)
            carry = 1 if addition > 9 else 0

            l1 = l1.next
            res = res.next
        
        while l2:
            addition = (l2.val + carry) 
            res.next =  ListNode(addition % 10)
            carry = 1 if addition > 9 else 0
            l2 = l2.next
            res = res.next

        if carry:
            res.next = ListNode(1, None)

        return dummy.next