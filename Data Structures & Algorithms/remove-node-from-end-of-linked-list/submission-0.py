# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        # Traverse to find the length
        l = self.findListLen(head)
        # Index of the node to be removed
        ind = l - n
        # Remove at ind
        if ind == 0:
            # Special case: Remove head node
            return head.next
        else:
            prev = head
            cur = head.next
            for _ in range(ind - 1):
                cur = cur.next
                prev = prev.next
            prev.next = cur.next
        return head

    def findListLen(self, head: Optional[ListNode]) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l
