'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #Created a list to store values for all list elements
        arr = []
        for l in lists:
            
            while l:
                arr.append(l.val)
                l = l.next
        
        #Sorting the array containing values from all lists
        arr = sorted(arr)
        #Creating a dummyNode which will assist in creating a sorted list
        dummyNode = ListNode(0)
        #head is set to the dummyNode
        #this is done to return head.next which
        #is the sorted list
        head = dummyNode
        for value in arr:
            dummyNode.next = ListNode(value)
            dummyNode = dummyNode.next
            
        return head.next
            
                
        
        
     
                

                
            
            
       
        
        
        
        
        
        
            
        