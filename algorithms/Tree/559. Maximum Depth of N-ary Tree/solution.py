class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node', depth=0) -> int:
        if root is None:
            return depth
        if root.children == []:
            return depth + 1
        depths = []
        for child in root.children:
            depths.append(self.maxDepth(child, depth + 1))
        return max(depths)
