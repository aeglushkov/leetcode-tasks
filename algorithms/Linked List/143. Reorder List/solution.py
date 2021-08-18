class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        node = head
        i = 1
        j = len(vals) - 1
        while j - i >= 0:
            if i == j:
                node.next = ListNode(vals[i])
            else:
                node.next = ListNode(vals[j])
                node = node.next
                node.next = ListNode(vals[i])
            node = node.next
            i += 1
            j -= 1
