# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return
        if not head.next:
            t = RandomListNode(head.label)
            if head.random:
                t.random = t
            return t
        t = head
        while t:
            new_one = RandomListNode(t.label)
            if t.next:
                new_one.next = t.next
                t.next = new_one
            else:
                t.next = new_one
            t = t.next.next
        t = head
        while t:
            if t.random:
                t.next.random = t.random.next
            t = t.next.next
        t = head
        p = head
        res = head.next
        while p:
            if p.next.next:
                p = p.next.next
                t.next.next = t.next.next.next
                t.next = p
                t = p
            else:
                t.next = None
                return res