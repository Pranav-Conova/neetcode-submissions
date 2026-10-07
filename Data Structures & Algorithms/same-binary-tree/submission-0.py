# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
            a = 1
            if (p is None and q is None) or (p and q and (p.val == q.val)):
                a =1
            else:
                a = 0
            if p is not None and q is not None:
                return min(same_tree(p.left, q.left), same_tree(p.right, q.right), a)
            else:
                return a
        return bool(same_tree(p, q))
            