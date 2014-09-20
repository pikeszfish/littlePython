# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                node = slow
                start = head
                while start is not node:
                    start = start.next
                    node = node.next
                return node

        if (not slow.next) or (not fast.next) or (not fast.next.next):
            return None