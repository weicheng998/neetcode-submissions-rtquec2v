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

        while cur_l1 and cur_l2:
            digit_sum = cur_l1.val + cur_l2.val + carry
            carry, digit_sum = divmod(digit_sum, 10)
            cur_res.next = ListNode(digit_sum)

            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            cur_res = cur_res.next
        
        while cur_l1:
            digit_sum = cur_l1.val + carry
            carry, digit_sum = divmod(digit_sum, 10)
            cur_res.next = ListNode(digit_sum)

            cur_l1 = cur_l1.next
            cur_res = cur_res.next


        while cur_l2:
            digit_sum = cur_l2.val + carry
            carry, digit_sum = divmod(digit_sum, 10)
            cur_res.next = ListNode(digit_sum)

            cur_l2 = cur_l2.next
            cur_res = cur_res.next
        
        if carry:
            cur_res.next = ListNode(carry)
        
        return res.next
