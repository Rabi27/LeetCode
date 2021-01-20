# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        lis = []
        
        def inorder(root):
        
            if root == None:
                return root
            
          
            inorder(root.left)
            lis.append(root.val)
            inorder(root.right)
            
            
        inorder(root)
            
        return lis 
        