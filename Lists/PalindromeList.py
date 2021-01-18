'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        
        temp = head
        lis = []
        while temp != None:
            
            lis.append(temp.val)
            temp = temp.next
            
        left = 0
        right = len(lis)-1
        
        while left <= right:
            
            if lis[left] != lis[right]:
                return False
            left += 1
            right -= 1
            
        return True 
            
       
            
            
        