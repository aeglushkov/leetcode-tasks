class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = self.get_inorder_traversal(root)
        return ans
    
    def get_inorder_traversal(self, node):
        if node is None:
            return []
        if node.left is None:
            right = self.get_inorder_traversal(node.right)
            return [node.val] + right
        if node.right is None:
            left = self.get_inorder_traversal(node.left)
            return left + [node.val]
        left = self.get_inorder_traversal(node.left)
        right = self.get_inorder_traversal(node.right)
        return  left + [node.val] + right
