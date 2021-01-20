# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
      
        if root is None:
            return root
    
       
        #If the key to be deleted less than root node than goto the left substree.
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
    
        #If the key to be deleted greater than root node than goto the right substree.
        elif(key > root.val):
            root.right = self.deleteNode(root.right, key)
    
        # If key is same as root's key, then this is the node to be deleted
        else:
    
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
    
            elif root.right is None:
                temp = root.left
                root = None
                return temp
    
            # Now solving for Node with two children: 
            # Get the inorder successor
            temp = self.minValueNode(root.right)
    
            # Copy the inorder successor's 
            # content to this node
            root.val = temp.val
    
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)
    
        return root
    
    def minValueNode(self,node):
        current = node
    
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left
    
        return current
    
        