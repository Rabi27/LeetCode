
'''
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head2 = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
            
        return head2
            