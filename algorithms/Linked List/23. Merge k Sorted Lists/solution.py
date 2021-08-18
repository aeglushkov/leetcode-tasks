class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = node = ListNode(0)
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        for val in sorted(vals):
            node.next = ListNode(val)
            node = node.next
        return head.next
