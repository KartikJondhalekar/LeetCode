# Problem #234: Palindrome Linked List
# Difficulty : Easy
# Language   : python3
# Runtime    : 34 ms
# Memory     : 34.8 MB
# URL        : https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head or not head.next:
#             return True
        
#         prev = None        
#         n = 0        
#         temp = head
        
#         while temp:
#             n += 1
#             temp = temp.next
            
#         mid = (n // 2) if (n % 2 == 0) else (n // 2) + 1
#         n = 1
        
#         temp = head
        
#         while n <= mid:            
#             temp = temp.next
#             n += 1
            
#         curr = temp
               
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
            
#         while prev:
#             if head.val != prev.val:
#                 return False
            
#             head = head.next
#             prev = prev.next
            
#         return True

        if not head or not head.next:
            return True
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
            
        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        left, right = head, prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
        
            
        