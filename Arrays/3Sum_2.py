'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        output = []
        nums.sort()
        
        for i in range(len(nums)-2):
            
            #If number at i and i-1 index are same
            #the continue statement would skip the code below it and will start over 
            #from the next loop
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = len(nums)-1
            
            while left < right:
                currSum =  nums[i] + nums[left] + nums[right] 
                if currSum < 0:
                    left += 1
                elif currSum > 0:
                    right -= 1
                elif  currSum == 0:
                    output.append([nums[i],nums[left],nums[right]])
                    #The while loops below are executed so as to avoid duplicates in the output
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1
                    
        return output
        
                        
                        