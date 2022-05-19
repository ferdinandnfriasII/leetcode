#leetcode practice question 141
#determine if a linked list contains a cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Using a hashset, we map the position of each node as the key and the node as the value
        if the pos input value is in the hashset then return true because there is a cycle.
        if pos is -1 or not in hashset return false
        """
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        """
        This code runs in O(n) time and space because we are using a hashset which occupies more memory
        
        nodeVisited = set()
        
        while head:
            if head in nodeVisited:
                return True
            nodeVisited.add(head)
            head = head.next
        return False
        """