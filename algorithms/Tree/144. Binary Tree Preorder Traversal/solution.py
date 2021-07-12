class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        left_traversal = self.preorderTraversal(root.left)
        right_traversal = self.preorderTraversal(root.right)
        return [root.val] + left_traversal + right_traversal
