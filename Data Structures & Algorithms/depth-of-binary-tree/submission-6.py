# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def breadth_first_search(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        levels: int = 0
        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                tmp = queue.popleft()
                if tmp and tmp.left:
                    queue.append(tmp.left)
                if tmp and tmp.right: 
                    queue.append(tmp.right)
            levels += 1
        return levels

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.breadth_first_search(root)
