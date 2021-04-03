class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans = [None]*len(nums)
        nums2 = nums+nums
        print(nums2)
        for i in range(len(nums)):
            ans[i] = -1
            for j in range((i+1)%len(nums2),len(nums2)):
                
                if nums2[j] > nums[i]:
                    ans[i] = nums2[j]
                    break
           
                
        
        return ans
        
                
        
        
