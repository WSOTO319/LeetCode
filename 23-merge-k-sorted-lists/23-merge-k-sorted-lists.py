# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: #if list is null or length is zero
            return None # return none

        while len(lists) > 1:#while length of list is greater than 1 
            mergedLists = []#initialize new list for merge
            for i in range(0, len(lists), 2):# iterate through each list 
                l1 = lists[i] # list 1 will be at index i 
                l2 = lists[i + 1] if (i + 1) < len(lists) else None #list 2 will be at i + 1 and if out of bounds then return an empty list 
                mergedLists.append(self.mergeList(l1, l2)) #use function and append lists to mergeLists
            lists = mergedLists#update lists variable to equal mergeLists  
        return lists[0]# return lists[0]

    def mergeList(self, l1, l2): #helper function that actually merges lists
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next