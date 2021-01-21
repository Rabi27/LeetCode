# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        
        if not head or not head.next:
            return head
        
        #An additional vairable is here temp
        #temp will be the address of the node 
        #previous to the middle node
        #It's next will be set ot None
        #so that the list could be splitted properly.
        #A new list splitted list is formed
        #from head to temp via setting temp.next to None
        fast = slow = temp = head
      

        while fast and fast.next:
            temp =slow
            slow = slow.next
            fast = fast.next.next
            
        temp.next = None
         
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.merge(left,right)
        
    

    def merge(self,l,r):
        dummy = ListNode(-1)
        h = dummy

        while l and r:

            if l.val < r.val:
                dummy.next = l
                l = l.next
            else:
                dummy.next = r
                r = r.next
            dummy = dummy.next
            
        if l:
             dummy.next = l 
        elif r:
            dummy.next = r
            
        return h.next




            
            
            
                
                
        
        
        
        
        