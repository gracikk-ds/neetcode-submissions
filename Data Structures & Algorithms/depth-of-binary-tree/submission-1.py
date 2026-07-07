# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth_first_search(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.depth_first_search(root.left), self.depth_first_search(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth_first_search(root)
