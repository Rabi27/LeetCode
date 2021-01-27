'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        #if head is None simply return head
        if not head: return head
        
        #find the mid the linKedList using the helper function findMid
        mid = self.findmid(head)
        #Set the root of the tree to value of the mid 
        root = TreeNode(mid.val)
        
        #if the addresses of mid node and head are same
        #that implies list has only one node
        #thus return the root of the tree
        if head == mid:
            return root
        #to construct the left and substree of the tree, 
        #recursively call the function again
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
        
        
    def findmid(self,head):
        fast = head
        slow = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        
        if prev:
            prev.next = None
        
        return slow
        
      
            
            
        
        
        
          
        
        
        