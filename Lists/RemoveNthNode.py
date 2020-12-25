# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        temp = head
        index = self.size_of_list(head) - n + 1

        for i in range(1,index-1):
            temp = temp.next

        temp.next = temp.next.next

        

    def print_list(self,head):

        temp = head
        while(temp != None):
            print(temp.val)
            temp = temp.next

    def size_of_list(self,head):

        temp = head
        count = 0
        while temp != None:
            count = count +1
            temp =temp.next
        return count


l5 = ListNode(14)
l4 = ListNode(11,l5)
l3 = ListNode(9,l4)
l2 = ListNode(7,l3)
l1 = ListNode(5,l2)


head = l1

r = Solution()
r.print_list(head)
print("Size of list:",r.size_of_list(head))

r.removeNthFromEnd(head,5)
r.print_list(head)