'''
229. Majority Element II
Medium

2458

215

Add to List

Share
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for v in set(nums):
            
            if nums.count(v) > (len(nums)//3):
                ans.append(v)
                
        return ans
                
        
        
