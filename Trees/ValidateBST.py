'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root == None: return None
       
        arr = []
        
        def inorder(root):
            
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
         
        
        #Getting inorder array elements
        inorder(root)
        
        #If the lengths are not same, it 
        #means the list contains duplicates
        if len(arr) != len(set(arr)):
            return False
        
        #Creating a new array
        #It will be a sorted version of arr
        newarr = sorted(arr)
        
        #If the newarr and arr are equal that means 
        #its a BST, else its not
        return newarr == arr
        

        
        
            
            
            
        