# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root: return None
        elif not root.left and not root.right and sum - root.val == 0:
            return True
        else:
            result = self.hasPathSum(root.left,sum-root.val)
            if result == True:
                return True
            result = self.hasPathSum(root.right,sum-root.val)
            if result == True:
                return True
        
        
        
                
        
      
        
        
        
        
    
    
    
            
        