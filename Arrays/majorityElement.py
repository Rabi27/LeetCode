class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)//2
        
        for i in range(len(nums)):
            
            if nums.count(nums[i]) > n:
                return nums[i]