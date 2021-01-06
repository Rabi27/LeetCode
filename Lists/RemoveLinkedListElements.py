'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


'''


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while head != None and head.val == val:
            head = head.next
        
        temp = head
        
        while temp != None and temp.next != None:
            
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
            
      
                
       
        return head