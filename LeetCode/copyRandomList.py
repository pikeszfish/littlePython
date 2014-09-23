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
            t.next = head.next
            t.random = head.random
            return t
        t = head
        while t:
            new_one = RandomListNode(0)
            if t.next:
                new_one.next = t.next
                t.next = new_one
            else:
                new_one.next = None
                t.next = new_one
                break
            t = t.next.next
        t = head
        while t:
            if t.random:
                t.next.random = t.random.next
            t = t.next.next
        t = head
        p = head
        while p:
            if p.next.next:
                p = p.next.next
                t.next.next = t.next.next.next
                t.next.random = t.random
                t = t.next.next
            else:
                t.next.next = None
                t.next.random = t.random
                break
        return head.next
