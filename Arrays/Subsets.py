'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset = [[]]
        
        for i in range(len(nums)):
            '''
            nums = [1,2,3]
            Iteration 1
            nums[i] = 1
            curr = []
            
            curr+nums[i] = [1]
            subset = [[],[1]]
            
            Iteration 2
            nums[i] = 2
            subset has two items, i.e [] and [1]
            now nums[i] = 2, will be merged with these
            items and generate a new list,
            that is curr + nums[i] = [] + [2] = [2]
            and with curr = [1] .... it is ... curr + nums[i] = [1] + [2] = [1,2]
            ... and so on
            '''
            
            subset += [curr+[nums[i]] for curr in subset]
            
        return subset
        
        
                
                
                
        

