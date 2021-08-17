class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left_node = l1
        right_node = l2
        head = node = ListNode(0)
        while left_node and right_node:
            if left_node.val > right_node.val:
                node.next = right_node
                right_node = right_node.next
            else:
                node.next = left_node
                left_node = left_node.next
            node = node.next
        node.next = left_node or right_node
        return head.next
