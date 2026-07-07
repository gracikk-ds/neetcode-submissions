"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {None: None}

        current = head
        while current:
            new = Node(current.val)
            hash_map[current] = new
            current = current.next

        current = head
        while current:
            new = hash_map[current]
            new.next = hash_map[current.next]
            new.random = hash_map[current.random]
            current = current.next
        
        return hash_map[head]