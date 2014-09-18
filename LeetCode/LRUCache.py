class Element:
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.mapping = {}
        self.head = None
        self.tail = None
        self.size = 0

    def append_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.pre = node
        self.head = node

    def del_tail(self):
        self.tail = self.tail.pre
        self.mapping.pop(self.tail.next.key)
        self.tail.next = None

    def move_to_head(self, node):
        if node is self.head:
            return
        if node is self.tail:
            self.tail = self.tail.pre
            self.tail.next = None
            node.pre = None
            node.next = self.head
            # do not forget!
            self.head.pre = node
            self.head = node
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = self.head
        # do not forget!
        self.head.pre = node
        self.head = node
        return

    # @return an integer
    def get(self, key):
        if key in self.mapping:
            node = self.mapping[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Element(key, value)
            self.size += 1
            self.mapping[key] = node
            self.append_to_head(node)
            if self.size > self.capacity:
                self.del_tail()
                self.size -= 1