class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self._remove(node)
            self._insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self._remove(node)
            self._insert(node)
        else:
            if len(self.cache) == self.capacity:
                node_to_remove = self.tail.prev
                del self.cache[node_to_remove.key]
                self._remove(node_to_remove)
            node_to_insert = Node(key, value)
            self.cache[key] = node_to_insert
            self._insert(node_to_insert)

    def _remove(self, node: Node) -> None:
        """
        Unlink a node from wherever it currently sits in the list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _insert(self, node: Node) -> None:
        """
        Insert a node at the most recently used end - head.
        """
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
