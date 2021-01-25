'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        if nums[0] == 0: return -1 
        
        ladder = nums[0] #Maximum Ladder
        stair = nums[0] #current ladder
        jump = 1
        
        for i in range(1,len(nums)):
            if i == len(nums)-1: return jump
            
            if nums[i] + i > ladder:
                ladder = nums[i] + i
                
            
            stair -= 1
            
            if stair == 0:
                jump += 1
                if i>= ladder: return -1
                stair = ladder - i
                
        
        return -1
                
        