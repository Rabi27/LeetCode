'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        temp = head
        l1 = ListNode(0)
        l2 = ListNode(0)
        h1 = l1
        h2 = l2
        
        
        while temp:
            
            if temp.val < x:
                l1.next = ListNode(temp.val)
                l1 = l1.next
            else:
                l2.next = ListNode(temp.val)
                l2 = l2.next
            
            temp = temp.next
            
        l1.next = h2.next
        
        return h1.next
            
        