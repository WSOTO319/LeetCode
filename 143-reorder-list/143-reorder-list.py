# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next #initialize slow and fast pointer 
        
        #find middle
        while fast and fast.next: #while the node at the fast pointer and the node following it are not null 
            slow = slow.next # move the slow pointer by 1
            fast = fast.next.next #move ther fast pointer by 2
            
            
        #reverse second half   
        second = slow.next # initialize the second variable to the next node of the low pointer(basically the first node of the second hald of the list)
        prev = slow.next = None # set prev variabe and next node to null (basically spliting the two halfs)
        
        while second: # while second is not null
            tmp = second.next # set temporary variable to next node
            second.next = prev # set the next node to the previous variable value
            prev = second # set prev now to equal the second variable 
            second = tmp # set second variabe to the value of temporary variable
            
        #merge two halfs 
        first, second = head, prev # initialize the first vairable to the head and the second variable to the value of the prev variable 
        while second: # while second is not null
            tmp1, tmp2 = first.next, second.next# temporary varaibles are set to the next node of first and second 
            first.next = second # node after first is now equal to value of second variable
            second.next = tmp1 # node after second is now equal to value of tmp1 variable 
            first,second = tmp1, tmp2 # set first and second to values of the temporary variables
            
            
# this code is more understandable with a visual and keeping track of all variables 