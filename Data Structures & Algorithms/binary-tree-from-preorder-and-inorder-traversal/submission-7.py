# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {val: idx for idx, val in enumerate(inorder)}

        def buildTreeHelper(
            preorder_start: int,
            preorder_end: int,
            inorder_start: int,
            inorder_end: int,
        ) -> Optional[TreeNode]:
            if inorder_start >= inorder_end or preorder_start >= preorder_end:
                return None

            root_val = preorder[preorder_start]
            idx = inorder_dict[root_val]
            left_size = idx - inorder_start

            root = TreeNode(root_val)
            root.left = buildTreeHelper(
                preorder_start + 1,
                preorder_start + 1 + left_size,
                inorder_start,
                idx,
            )
            root.right = buildTreeHelper(
                preorder_start + 1 + left_size,
                preorder_end,
                idx + 1,
                inorder_end,
            )
            return root

        return buildTreeHelper(0, len(preorder), 0, len(inorder))
