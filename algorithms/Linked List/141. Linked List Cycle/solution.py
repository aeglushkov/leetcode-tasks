class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    # Solution 1
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        visited = dict()
        while node is not None:
            if visited.get(node):
                return True
            visited[node] = True
            node = node.next
        return False
    
    # Solution 2
    def hasCycle2(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
