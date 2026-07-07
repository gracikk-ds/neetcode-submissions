# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                tmp, left, right = queue.popleft()

                if not (left < tmp.val < right):
                    return False

                if tmp.left:
                    queue.append([tmp.left, left, tmp.val])
                
                if tmp.right:
                    queue.append([tmp.right, tmp.val, right])

        return True