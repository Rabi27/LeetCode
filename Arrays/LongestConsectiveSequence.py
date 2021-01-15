'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Follow up: Could you implement the O(n) solution? 

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        nums.sort()
        count = 1
        maxcount = 1
        
        for i in range(len(nums)-1):
            
            if nums[i+1] == nums[i]+1:
                count += 1
            elif nums[i] == nums[i+1]:
                pass
            else:
                if count > maxcount:
                    maxcount = count 
                count = 1
                
        return maxcount if maxcount>count else count 
                
            
        