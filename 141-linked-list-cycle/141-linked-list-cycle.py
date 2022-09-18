# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head #slow and fast pointer initiated
        
        while fast and fast.next: # while node at fast pointer is not null and next node is not null
            slow = slow.next #move slow pointer up by one node
            fast = fast.next.next # move fast pointer up by two nodes
            if slow == fast: # if node at slow pointer and fast pointer are the same, return true 
                return True
            
        return False # if they never are at the same node return false