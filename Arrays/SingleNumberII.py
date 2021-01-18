'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dic = {}
        
        
        for number in nums:
            
            if number not in dic:
                dic[number] = 1
            else:
                dic[number] += 1
                
        for k, v in dic.items():
            
            if v == 1:
                return k
        
        
                
        
        
       
                
            
            
            
            
                