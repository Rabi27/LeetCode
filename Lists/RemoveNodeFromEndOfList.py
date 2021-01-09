'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        count = 0 
        
        while temp != None:
            count = count + 1
            temp = temp.next
            
        length = count - n -1
        temp = dummy
        
        while length > 0:
            length = length - 1
            temp = temp.next
            
        temp.next = temp.next.next
        
        return dummy.next
            
       
        
     
            
            
        