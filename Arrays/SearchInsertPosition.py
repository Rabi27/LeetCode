'''
Given a sorted array of distinct integers and a target value, return the index if the target is 
found. If not, return the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif nums[i] > target:
                return i
            
        