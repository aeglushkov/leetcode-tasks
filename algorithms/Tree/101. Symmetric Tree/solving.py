class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ans = self.is_symmetric(root.left, root.right)
        return ans
    
    def is_symmetric(self, left_tree, right_tree):
        if left_tree is None and right_tree is None:
            return True
        if left_tree is None or right_tree is None:
            return False
        if left_tree.val == right_tree.val:
            is_left_sub_tree = self.is_symmetric(left_tree.left, right_tree.right) 
            is_right_sub_tree = self.is_symmetric(left_tree.right, right_tree.left)
            return is_left_sub_tree and is_right_sub_tree
        return False
