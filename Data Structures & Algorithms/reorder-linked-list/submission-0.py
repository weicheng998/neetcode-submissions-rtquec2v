# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split into 2 halves
        half1 = head
        half2 = self.findMidList(head)
        temp = half2.next
        half2.next = None
        half2 = temp
        # Reverse the 2nd half
        half2_reversed = self.reverseList(half2)
        # Merge
        res = ListNode()
        cur = res
        while half1 and half2_reversed:
            cur.next = half1
            cur = cur.next
            half1 = cur.next
            cur.next = half2_reversed
            cur = cur.next
            half2_reversed = half2_reversed.next
        if half1:
            cur.next = half1
        res = res.next
        head.val = res.val
        head.next = res.next

    def findMidList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head.next = None
        return prev
