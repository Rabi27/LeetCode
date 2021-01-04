# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        temp = head
        temp2 = head
        
        
        while temp != None:
            temp2 = temp.next 
            while temp2 != None:
                
                if temp.val > temp2.val:
                    a = temp.val
                    temp.val = temp2.val
                    temp2.val = a
                temp2 = temp2.next
            temp = temp.next
                    
        return head
        