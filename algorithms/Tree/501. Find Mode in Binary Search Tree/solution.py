class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        freq = self.counter(root, {})
        most_freq_el = [root.val]
        cnt = 1
        for key, value in freq.items():
            if value > cnt:
                cnt = value
                most_freq_el = [key]
            if value == cnt:
                if key not in most_freq_el:
                    most_freq_el.append(key)
        return most_freq_el
        
    def counter(self, node, freq):
        if node is None:
            return freq
        val = node.val
        if not freq.get(val):
            freq[val] = 1
        else:
            freq[val] += 1
        freq = self.counter(node.left, freq)
        freq = self.counter(node.right, freq)
        return freq
