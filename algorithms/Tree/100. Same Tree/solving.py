# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        is_same = self.is_same(p, q)
        return is_same
    
    def is_same(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.is_same(p.left, q.left) and self.is_same(p.right, q.right)
        return False
