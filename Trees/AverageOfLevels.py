'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        
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
               
             
            avg = sum(layer)/len(layer)    
            result.append(avg)
            
        return result
        