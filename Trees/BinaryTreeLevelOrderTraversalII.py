'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if root is None: return None
        
        queue = [root]
        result = []
    
    
        while queue != []:
            layer = []
            
            
            for i in range(len(queue)):
                #Remove the first element of the queue and save it in a variable
                node = queue[0]
                del queue[0]
                #Append its value in the layer array
                layer.append(node.val)
                #If there is a left node, insert it in the queue
                if node.left:
                    queue.append(node.left)
                #If there is a right node, insert it in the queue
                if node.right:
                    queue.append(node.right)
               
                
            result.append(layer)
            
        return result[::-1]
        