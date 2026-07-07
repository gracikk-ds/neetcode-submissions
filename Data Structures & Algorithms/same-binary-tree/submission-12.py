# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def ensure_same_nodes(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val

    def add_node_to_queue(self, node: Optional[TreeNode], queue) -> None:
        if node:
            queue.append(node.left)
        if node:
            queue.append(node.right)

    def bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue or q_queue:
            lenp = len(p_queue)
            lenq = len(q_queue)

            if lenp != lenq:
                return False

            for _ in range(lenp):
                tmpp = p_queue.popleft()
                tmpq = q_queue.popleft()

                issame = self.ensure_same_nodes(tmpp, tmpq)
                if not issame:
                    return issame

                self.add_node_to_queue(tmpp, p_queue)
                self.add_node_to_queue(tmpq, q_queue)

        return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p, q)
        