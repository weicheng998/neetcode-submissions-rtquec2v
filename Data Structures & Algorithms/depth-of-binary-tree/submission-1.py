# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        # Make sure all nodes in queue are not None
        if not root:
            return depth
        # BFS with a queue
        queue = deque([root])
        while queue:
            # Process all nodes at current level
            width = len(queue)
            for _ in range(width):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth
