# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        # Two pointers
        slow = fast = head
        # Move the fast pointer n nodes ahead
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        # Move both pointers together
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        # Slow should land on the prev node of removal
        if slow is head and not fast:
            # Special case
            head = head.next
        else:
            slow.next = slow.next.next
        return head