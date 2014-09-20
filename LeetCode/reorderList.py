# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        i = 0 
        t = head
        all = {}
        while t:
            all[i] = t
            i += 1
            t = t.next
        j = 0
        t = head
        while j < (i/2):
            t.next = all[i-1-j]
            j += 1
            t.next.next = all[j]
            t = t.next.next
        t.next = None
        return all[0]