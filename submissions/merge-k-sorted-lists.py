# Problem #23: Merge k Sorted Lists
# Difficulty : Hard
# Language   : python3
# Runtime    : 8 ms
# Memory     : 20 MB
# URL        : https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(list1, list2):
            dummy = ListNode()
            resList = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next

                dummy = dummy.next
            
            dummy.next = list1 if list1 else list2

            return resList.next

        # res = None

        # for node in lists:
        #     res = merge(res, node)

        # return res

        if not lists:
            return None

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]