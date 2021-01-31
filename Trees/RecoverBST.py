'''
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #This list will contains addresses of nodes
        nodes = []
        #This list will contain values of nodes
        nodevalues = []
        
        
        
        def inorder(root):
            
            if root:
                inorder(root.left)
                nodes.append(root)
                nodevalues.append(root.val)
                inorder(root.right)
          
        #Inorder traversal fills values of nodes and nodevalues
        inorder(root)
      
        #Now we get a sorted list of nodevalues ...
        #The sequence of nodevalues_sorted is the actual sequence of the BST
        nodevalues_sorted = sorted(nodevalues)
        #This will stores indexes when values nodevalues list and nodevalues_sorted
        #are compared. If the values of the two list mismatch, then index will added to
        #to the indexes list. Indexes will contain index of both nodes whose value needed
        #to be swapped
        indexes = []
        
        for i in range(len(nodevalues)):
            
            if nodevalues[i] != nodevalues_sorted[i]:
                indexes.append(i)
        #Swapping values of nodes that invalidate the BST       
        temp = nodes[indexes[0]].val
        nodes[indexes[0]].val = nodes[indexes[1]].val
        nodes[indexes[1]].val = temp
        