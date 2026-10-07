# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def _depth_finder(root, count = 1):
            if root is None:
                return
            self.depth = max(self.depth, count)
            
            _depth_finder(root.right, count + 1)
            _depth_finder(root.left, count + 1)
        _depth_finder(root)
        return self.depth
        