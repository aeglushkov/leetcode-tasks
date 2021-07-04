# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root
    
    def invert(self, node):
        if not node:
            return
        if node.left is None and node.right is None:
            return
        if node.left is None:
            node.left = node.right
            node.right = None
            return self.invert(node.left)
        if node.right is None:
            node.right = node.left
            node.left = None
            return self.invert(node.right)
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
