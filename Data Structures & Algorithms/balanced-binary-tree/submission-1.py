# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Unbalanced(Exception):
    pass


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            if abs(left_depth - right_depth) > 1:
                raise Unbalanced()
            return max(left_depth, right_depth) + 1

        try:
            depth(root)
            return True
        except Unbalanced:
            return False
