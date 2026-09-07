# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = deque()
        count = 1

        while cur or stack:
            # Reach the deepest left node
            while cur:
                stack.append(cur)
                cur = cur.left

            # Cur must be None, so pop from stack
            cur = stack.pop()
            if count == k:
                return cur.val
            count += 1

            # Left and Node are processed, now Right
            cur = cur.right
        
        raise ValueError()
