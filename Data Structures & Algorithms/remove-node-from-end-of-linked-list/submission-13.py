# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftp = head
        rightp = head

        for _ in range(n):
            rightp = rightp.next

        prev = None
        while rightp:
            prev = leftp
            leftp = leftp.next
            rightp = rightp.next 
        
        if prev:
            prev.next = leftp.next
        else:
            head = leftp.next
        return head