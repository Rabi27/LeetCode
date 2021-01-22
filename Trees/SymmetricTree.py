'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root == None: return True
        
        queue = [root,root]
        
    
        while queue != []:
            NodeA = queue[0]
            NodeB = queue[1]
            del queue[0]
            del queue[0]
            
            if NodeA == None and NodeB == None: continue
            if NodeA == None or NodeB == None: return False
            if NodeA.val != NodeB.val: return False
            
            queue.append(NodeA.left)
            queue.append(NodeB.right)
            queue.append(NodeA.right)
            queue.append(NodeB.left)
            
        return True
        
       
        