# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # compute num nodes
        current = head
        count_nodes = 1
        while current.next:
            count_nodes += 1
            current = current.next

        idx_to_be_removed = count_nodes - n 
        print(idx_to_be_removed)

        prev = None
        current = head
        for idx in range(idx_to_be_removed + 1):
            tmp = current.next
            if idx == idx_to_be_removed:
                if prev is not None:
                    prev.next = tmp
                    return head
                head = tmp
                return head
            prev = current
            current = tmp


        