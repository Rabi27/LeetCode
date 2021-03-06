'''
1315. Sum of Nodes with Even-Valued Grandparent
Medium

802

32

Add to List

Share
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        queue = [root]
        temp = []
        s = 0
        
        while queue:
            
            for i in range(len(queue)):
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right)
                
                if node.val%2 == 0:
                    while temp:
                        n = temp.pop(0)
                        if n.left:
                            s += n.left.val
                        if n.right:
                            s += n.right.val
                temp = []
        
        return s
                        
                    
                    
                
        