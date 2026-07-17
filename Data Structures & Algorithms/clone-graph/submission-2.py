"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        storage = {}

        if node is None:
            return 

        def dfs(node: Node) -> Node:
            if node in storage:
                return storage[node]

            copy = Node(val=node.val)
            storage[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        copy = dfs(node)
        return copy