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
        # Pass 1
        # For each node A, insert a copy A' right after it
        cur = head
        while cur:
            temp = cur.next
            cur.next = Node(x=cur.val, next=temp)
            cur = cur.next.next
        
        # Pass 2
        # Wire up A'.random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next

        # Pass 3
        # Split the copies and the original nodes
        cur_new = head_new = Node(0)
        cur_old = head
        while cur_old:
            cur_new.next = cur_old.next
            temp = cur_old.next.next
            cur_old.next = temp
            cur_new.next.next = None
            cur_old = cur_old.next
            cur_new = cur_new.next
        
        return head_new.next