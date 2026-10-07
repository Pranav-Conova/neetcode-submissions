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
            queue = [root]
            
            # Loop until the list is empty
            while len(queue) > 0:
                # Remove the first element from the list
                current_node = queue.pop(0)
                
                # Check if this is the target node
                if current_node.val == subRoot.val:
                    if isSame(current_node, subRoot):
                        return True
                    
                # Add the left child to the back of the list if it exists
                if current_node.left:
                    queue.append(current_node.left)
                    
                # Add the right child to the back of the list if it exists
                if current_node.right:
                    queue.append(current_node.right)
                    
            # Return None if the target value was not found
            return False
        return find_root_node(root, subRoot)