class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        self.get_root2leaf_paths(root, ans, '')
        return ans
    
    def get_root2leaf_paths(self, node, paths, path):
        if node is None:
            return 
        if node.left is None and node.right is None:
            paths.append(path + str(node.val))
            return 
        path = path + str(node.val)
        left_path = self.get_root2leaf_paths(node.left, paths, path + '->')
        right_path = self.get_root2leaf_paths(node.right, paths, path + '->')
        return 
