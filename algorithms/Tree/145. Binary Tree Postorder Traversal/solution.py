class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        left_traversal = self.postorderTraversal(root.left)
        right_traversal = self.postorderTraversal(root.right)
        return left_traversal + right_traversal + [root.val]
