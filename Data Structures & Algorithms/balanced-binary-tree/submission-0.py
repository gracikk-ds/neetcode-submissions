# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True

    def dfs(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left - right) > 1:
            self.is_balanced = False
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.dfs(root)
        return self.is_balanced
        