# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    num_good_nodes: int = 0

    def dfs(self, root: TreeNode, max_val: int) -> bool:
        if not root:
            return 0

        if root.val >= max_val:
            self.num_good_nodes += 1
            max_val = root.val

        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root, root.val)
        return self.num_good_nodes
