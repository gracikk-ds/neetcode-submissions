# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node: Optional[TreeNode], depth) -> None:
        if not node:
            return 
        self.dfs(node.left, depth + 1)
        self.sorted_val.append(node.val)
        self.dfs(node.right, depth + 1)
        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_val = []
        self.dfs(root, 0)
        return self.sorted_val[k-1]
        