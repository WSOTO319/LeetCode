# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # previous variable is set to none by default
        while head: # while not at end of list
            curr = head # current variable is set to the value of the head variable
            head = head.next # head variable is set to the next value(basically moving the head variable towards the right each loop)
            curr.next = prev # next value in list is set to value of previous variable( basically making the previous value, the nxt nodes value)
            prev = curr # previous variable is set to value of curr variable
        return prev # return prev as it is now the new head of the list