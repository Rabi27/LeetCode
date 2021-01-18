'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        dic = {}
        
        
        for number in nums:
            
            if number not in dic:
                dic[number] = 1
            else:
                dic[number] += 1
                
        lis = []
                
        for k, v in dic.items():
            
            if v == 1:
                lis.append(k)
                
        return lis
        