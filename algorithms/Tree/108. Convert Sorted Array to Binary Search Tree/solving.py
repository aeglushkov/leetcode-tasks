class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        tree = self.build_tree(nums, TreeNode(val=None))
        return tree
    
    def build_tree(self, nums, tree):
        if len(nums) == 0:
            return tree
        if len(nums) == 1:
            tree.val = nums[0]
            return tree
        mid = len(nums) // 2
        left = 0
        right = len(nums)
        tree.val = nums[mid]
        tree.left = self.build_tree(nums[left : mid], TreeNode(val=None))
        tree.right = self.build_tree(nums[mid + 1 : right], TreeNode(val=None))
        if tree.right.val is None:
            tree.right = None
        return tree
