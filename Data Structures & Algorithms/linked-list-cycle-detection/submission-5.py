# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        list_set = set()
        current = head
        while current:
            if current in list_set:
                return True
            list_set.add(current)
            current = current.next
        return False
