# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        cur_res = res = ListNode(0)
        carry = 0

        while cur_l1 or cur_l2 or carry:
            val1 = cur_l1.val if cur_l1 else 0
            val2 = cur_l2.val if cur_l2 else 0
            carry, digit_sum = divmod(val1 + val2 + carry, 10)
            cur_res.next = ListNode(digit_sum)

            cur_res = cur_res.next
            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None

        return res.next
