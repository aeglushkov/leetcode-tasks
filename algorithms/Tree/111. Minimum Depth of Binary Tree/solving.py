class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ans = self.get_min_depth(root)
        return ans
    
    def get_min_depth(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            return self.get_min_depth(node.right) + 1
        if node.right is None:
            return self.get_min_depth(node.left) + 1
        left_depth = self.get_min_depth(node.left) + 1
        right_depth = self.get_min_depth(node.right) + 1
        return min(left_depth, right_depth)
