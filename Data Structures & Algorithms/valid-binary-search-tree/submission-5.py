# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isValidHelper(node: Optional[TreeNode], lower, upper) -> bool:
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return isValidHelper(node.left, lower, node.val) and isValidHelper(
                node.right, node.val, upper
            )

        return isValidHelper(root, float("-inf"), float("inf"))
