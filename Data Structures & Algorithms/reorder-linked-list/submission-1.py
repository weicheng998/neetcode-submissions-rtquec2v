class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Split into 2 halves
        half1 = head
        half2 = self.findMidList(head)
        temp = half2.next
        half2.next = None
        half2 = temp

        # Reverse the 2nd half
        half2_reversed = self.reverseList(half2)

        # Merge directly, relinking head's own chain
        while half2_reversed:
            n1 = half1.next
            n2 = half2_reversed.next

            half1.next = half2_reversed
            half2_reversed.next = n1

            half1 = n1
            half2_reversed = n2

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
