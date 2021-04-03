class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = [None]*len(nums1)
        
        
        for i in range(len(nums1)):
            
            for j in range(nums2.index(nums1[i])+1,len(nums2)):
                
                if nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
            
            if ans[i] == None:
                ans[i] = -1
                
        
        return ans
