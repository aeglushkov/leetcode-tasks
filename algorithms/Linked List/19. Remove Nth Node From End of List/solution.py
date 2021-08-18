class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        prev_node = head
        k = 0
        while node.next is not None:
            if k > n - 1:
                prev_node = prev_node.next
            k += 1
            node = node.next
        if k <= n - 1:
            head = head.next
        if prev_node == node:
            return None
        prev_node.next = prev_node.next.next
        return head
