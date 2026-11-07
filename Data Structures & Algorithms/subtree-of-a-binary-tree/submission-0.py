# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        def find_root_node(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if root and root.val == subRoot.val:
                return isSame(root, subRoot)
            if root.left:
                find_root_node(root.left, subRoot)
            if root.right:
                find_root_node(root.right, subRoot)
        return bool(find_root_node(root, subRoot))