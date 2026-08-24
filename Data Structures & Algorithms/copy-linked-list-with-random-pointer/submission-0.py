"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # Dict: node_old -> node_new
        reference: dict[Optional[Node], Optional[Node]] = {}

        # Pass 1: Deep copy without .random and build reference
        cur_new = head_new = Node(0)
        cur_old = head
        while cur_old:
            node_new = Node(cur_old.val)
            reference[cur_old] = node_new
            cur_new.next = node_new
            cur_new = cur_new.next
            cur_old = cur_old.next
        head_new = head_new.next

        # Pass 2: Add .random relations
        cur_new = head_new
        cur_old = head
        while cur_old:
            rand = cur_old.random
            if not rand:
                cur_new.random = None
            else:
                cur_new.random = reference[rand]
            cur_new = cur_new.next
            cur_old = cur_old.next

        return head_new
