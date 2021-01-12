'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        if len(nums) == 1:
            return nums[0]
        
        product = 1
        maxproduct = nums[0]
        maxsubarr = []
        
        for i in range(len(nums)):

            #setting maxproduct to nums[i] is not a good approach given that 
            #when the outer loop is at the last index
            #in that case the inner loop is to be terminated
            #as a result the maxproduct value is set to nums[i] without the inner loop being executed

            #maxproduct = nums[i]
            product = nums[i]
            for j in range(i+1,len(nums)):
                product *= nums[j]
                maxproduct = max(product,maxproduct,nums[i])

                #if maxproduct == product:
                    #maxsubarr = nums[i:j+1]

        if maxproduct < nums[-1]:
            return nums[-1]
        
        return maxproduct

                
                
        