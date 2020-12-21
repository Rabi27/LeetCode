'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except
 the number 0 itself


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        l3 = ListNode(0)
        resultIterator = l3
        temp = l3
        sum = 0
        carry= False
        
        while l1 != None or l2 != None:
            sum = 0
            if l1 == None:
                sum = l2.val
                l2 = l2.next
            elif l2 == None:
                sum = l1.val
                l1 = l1.next
            else:
                sum = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
                
            if carry:
                sum = sum + 1
            
                
            if sum >= 10:
                sum = sum%10
                carry = True
            else:
                carry = False
                
            newNode = ListNode(sum)
            resultIterator.next = newNode
            resultIterator = resultIterator.next
            
        if carry:
            resultIterator.next = ListNode(1)
            
            
            
            
                
            
            
        return l3.next
                
            
            
            
        
        
        
        
        
        
            
        
        