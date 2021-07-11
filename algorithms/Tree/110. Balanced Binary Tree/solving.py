class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        ans = self.get_height(root)
        return ans
    
    def get_height(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            right_height = self.get_height(node.right)
            if right_height is False:
                return False
            diff = abs(right_height - 0)
            if diff > 1:
                return False
            return right_height + 1
        if node.right is None:
            left_height = self.get_height(node.left)
            if left_height is False:
                return False
            diff = abs(0 - left_height)
            if diff > 1:
                return False
            return left_height + 1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        if left_height is False or right_height is False:
            return False
        diff = abs(right_height - left_height)
        if diff > 1:
            return False
        return max(left_height, right_height) + 1