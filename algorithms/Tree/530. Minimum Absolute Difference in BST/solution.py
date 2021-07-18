class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        lst = self.tree2list(root)
        min_diff = 10 ** 5
        for i in range(len(lst) - 1):
            diff = lst[i + 1] - lst[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
    
    def tree2list(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        left_subtree = self.tree2list(node.left)
        right_subtree = self.tree2list(node.right)
        return left_subtree + [node.val] + right_subtree
