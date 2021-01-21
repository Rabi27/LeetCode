class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        if len(nums) > 1:
            
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]
            
            self.sortColors(L)
            self.sortColors(R)
            
            l = r = k = 0
            
            while l < len(L) and r < len(R):
                if L[l] < R[r]:
                    nums[k] = L[l]
                    l += 1
                else:
                    nums[k] = R[r]
                    r += 1
                k += 1
                
            while l < len(L):
                nums[k] = L[l]
                l += 1
                k += 1
            
            while r < len(R):
                nums[k] = R[r]
                r += 1
                k += 1
        
        