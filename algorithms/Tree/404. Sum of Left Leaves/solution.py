class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = self.get_sum_of_left_leaves(root, 0, False)
        return ans
    
    def get_sum_of_left_leaves(self, node, sum_, is_left):
        if node is None:
            return sum_
        if node.left is None and node.right is None:
            if is_left:
                return sum_ + node.val
            return sum_
        left_sum = self.get_sum_of_left_leaves(node.left, sum_, True)
        right_sum = self.get_sum_of_left_leaves(node.right, sum_, False)
        return left_sum + right_sum
