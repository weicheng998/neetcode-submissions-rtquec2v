# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def countGoodNodes(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            if node.val >= max_val:
                return (
                    1 + countGoodNodes(node.left, node.val) + countGoodNodes(node.right, node.val)
                )
            else:
                return countGoodNodes(node.left, max_val) + countGoodNodes(node.right, max_val)

        return countGoodNodes(root, root.val)
