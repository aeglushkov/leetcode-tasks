class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _, ans = self.get_diameter(root, 0)
        return ans
    
    def get_diameter(self, node, max_d):
        if node is None:
            return 0, 0
        if node.left is None and node.right is None:
            return 1, 0
        left_depth, max_d_1 = self.get_diameter(node.left, max_d)
        right_depth, max_d_2 = self.get_diameter(node.right, max_d)
        depth = max(left_depth, right_depth) + 1
        max_d = max(max_d_1, max_d_2)
        return depth, max(max_d, left_depth + right_depth)
