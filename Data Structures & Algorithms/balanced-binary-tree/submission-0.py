# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]):
            if root is None:
                return 0 
            return 1 + max(height(root.left), height(root.right))
        def isbalanced(root: Optional[TreeNode]):
            if root is None:
                return 1
            if abs(height(root.left) - height(root.right)) > 1:
                return 0
            return min(isbalanced(root.left), isbalanced(root.right))
        if isbalanced(root):
            return True
        else:
            return False
        