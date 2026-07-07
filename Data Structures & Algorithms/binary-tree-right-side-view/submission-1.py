# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        visible_nodes = []

        queue = deque([root])
        while queue:
            qlen = len(queue)

            isfirst = True
            for _ in range(qlen):
                tmp = queue.popleft()
                if isfirst:
                    visible_nodes.append(tmp.val)
                    isfirst = False
                if tmp.right:
                    queue.append(tmp.right)
                if tmp.left:
                    queue.append(tmp.left)
        return visible_nodes