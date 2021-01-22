'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        

        queue = [p,q]
        
    
        while queue != []:
            NodeA = queue[0]
            NodeB = queue[1]
            del queue[0]
            del queue[0]
            
            if NodeA == None and NodeB == None: continue
            if NodeA == None or NodeB == None: return False
            if NodeA.val != NodeB.val: return False
            
            queue.append(NodeA.left)
            queue.append(NodeB.left)
            queue.append(NodeA.right)
            queue.append(NodeB.right)
            
        return True
                    
        
        
   
        