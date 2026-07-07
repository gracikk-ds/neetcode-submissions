# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        prev_node = dummy
        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            val3 = prev_node.next.val if prev_node.next else 0
            result = val1 + val2 + val3
            main_digit = result // 10
            sup_digit = result % 10

            # add sup digit
            prev_node.next = ListNode(0, None)
            prev_node.next.val = sup_digit
            prev_node = prev_node.next

            # add main_digit if exists
            if main_digit != 0:
                prev_node.next = ListNode(0, None)
                prev_node.next.val = main_digit

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next