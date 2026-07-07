# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        array = []
        while head:
            array.append(head)
            head = head.next

        left = 0
        right = len(array) - 1

        while left < right:
            array[left].next = array[right]
            left += 1
            if left >= right:
                break
            array[right].next = array[left]
            right -= 1

        array[left].next = None 


        