# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    diameter = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter
