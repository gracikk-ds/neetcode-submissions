# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    condition = True

    def dfs(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        if abs(left_height - right_height) > 1:
            self.condition = False
        return 1 + max(self.dfs(root.left), self.dfs(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.condition
        