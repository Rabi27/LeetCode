'''

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        
        #If the list is empty or contains only one element i.e. head.next = None or the value of k is 0
        #Then simply return the head of the list
        if head == None or head.next == None or k == 0:
            return head
        
        temp = head
        count  = 0
        #Calculate the size of the list
        while temp != None:
            count += 1
            temp = temp.next
         
        
        #If the value of k is greater than the size of the list, 
        #then take modulus of k with the size of the list
        # Initiall I was using k = k -count
        #It worked for some test cases but for larger values of k it turned n value to negative
        if k > count:
            k = k % count
        
        n = count - k
        
        #If the value n is 0 or value of k is 0, i.e k is a multiple of size of the list
        #then return head
        if n == 0 or k == 0:
            return head
        
        #run the loop n-1 times to get address to get address of the new last node
        temp = head
        for i in range(n-1):
            temp = temp.next
        #temp now contains the new last node
        #the temp.next node is the new head of the list
        newHead = temp.next
        #to make temp the last node, setting temp.next to None
        temp.next = None
        
        #Looping through the new head till its last node
        #this step is done so as to make the last node of the newhead point to the previous head of the last
        temp = newHead
        while temp.next != None:
            temp = temp.next
         
        #Now the old last node points to to old head of the list
        temp.next = head
        #setting head equal to the new head
        head = newHead
        
        return head
        
    
        
        
            
        
        
        