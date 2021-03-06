'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None: return root
        
        q = [root]
        
        while q:
            
            for i in range(len(q)):
                current = q[0]
                del q[0]
                
                temp = current.left
                current.left = current.right
                current.right = temp
                
                
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
         
                
        return root
                
        