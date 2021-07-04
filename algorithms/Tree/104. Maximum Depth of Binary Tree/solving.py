# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = self.count_depth(root, 1)
        return count
        
    def count_depth(self, node, count):
        if node.left is None and node.right is None:
            return count
        if node.left is None:
            return self.count_depth(node.right, count + 1)
        if node.right is None:
            return self.count_depth(node.left, count + 1)
        return max(self.count_depth(node.left, count + 1), 
                   self.count_depth(node.right, count + 1))
