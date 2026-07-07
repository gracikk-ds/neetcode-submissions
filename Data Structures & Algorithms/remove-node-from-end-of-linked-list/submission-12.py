# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # compute num nodes
        count_nodes = 0
        current = head
        while current:
            count_nodes += 1
            current = current.next

        # compute idx to be removed
        idx_to_be_removed = count_nodes - n 
        if idx_to_be_removed == 0:
            return head.next

        # remove node by index
        current = head
        for idx in range(idx_to_be_removed + 1):
            if idx + 1 == idx_to_be_removed:
                current.next = current.next.next
                break
            current = current.next
        return head


        