'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None: return None
        
        queue = [root]
        result = []
        count = 0
    
    
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
                          
            count += 1
               
            if count%2 == 0: 
                newlayer = layer[::-1]
                result.append(newlayer)
            else:
                result.append(layer)
               
        
            
        return result
        
        