class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        a = [[] for i in range(2048)]
        depth = 1
        b = self.get_level_order(root, a, depth)
        b[0].append(root.val)
        ans = [el for el in b if el != []]
        return ans
    
    def get_level_order(self, node, a, depth):
        if node is None:
            return a
        children_nodes = self.get_children_nodes(node)
        if children_nodes is not None:
            for children_node in children_nodes:
                a[depth].append(children_node)
        a = self.get_level_order(node.left, a, depth + 1)
        a = self.get_level_order(node.right, a, depth + 1)
        return a
    
    def get_children_nodes(self, node):
        left = node.left
        right = node.right
        if left is None and right is None:
            return None
        if left is None:
            return [right.val]
        if right is None:
            return [left.val]
        return [left.val, right.val]
