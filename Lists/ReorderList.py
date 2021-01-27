'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
Accepted
300,849
Submissions
745,821
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        temp = head
        l = []
        while temp != None:
            l.append(temp)
            temp = temp.next
            
        left = 0
        right = len(l)-1
        last = None
        
        while left < right:
            l[left].next = l[right]
            left += 1
            
            if left == right:
                last = l[right]
                break
            
            l[right].next = l[left]
            right -= 1
            
            last = l[left]
            
        if last:
            last.next = None
        
        
        
        