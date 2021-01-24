'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        temp = head
        l1 = []
        l2 = []
        count = 0
        
        
        while temp != None:
            l1.append(temp.val)
            count +=1 
            if count == k:
                l2 = l2 +l1[::-1] 
                l1 = []
                count = 0
                
            temp = temp.next
            
        l2 = l2 + l1
        
        dummy = ListNode(0)
        h = dummy
        
        for  i in range(len(l2)):
            dummy.next = ListNode(l2[i])
            dummy = dummy.next
        
        return h.next
        
        
            
            
        
      
            