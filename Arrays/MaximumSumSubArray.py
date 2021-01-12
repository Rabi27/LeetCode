'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            
            curr_sum = 0
            for j in range(i,len(nums)):
                
                curr_sum += nums[j]
                max_sum = max(curr_sum,max_sum)
                
        return max_sum
        
        
    
        
        
        
        