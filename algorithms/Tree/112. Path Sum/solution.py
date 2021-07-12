class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        ans = self.is_have_path_sum(root, targetSum)
        return ans
    
    def is_have_path_sum(self, node, targetSum):
        if node is None:
            return targetSum == 0
        if node.left is None and node.right is None:
            return targetSum - node.val == 0
        left = self.hasPathSum(node.left, targetSum - node.val)
        right = self.hasPathSum(node.right, targetSum - node.val)
        return left or right
