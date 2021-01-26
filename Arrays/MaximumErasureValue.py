class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        i = 0
        j = 1
        
        subarr = [nums[0]]
        maxsize = 1
        arr = []
        
        while j < len(nums):
            
            if nums[j] not in subarr:
                subarr.append(nums[j])
            elif nums[j] in subarr:
                if len(subarr) > maxsize:
                    arr.append(subarr)
                    maxsize = len(subarr)
                i = subarr.index(nums[j])
                subarr = subarr[i+1:]
                subarr.append(nums[j])
            j += 1
        
        arr.append(subarr) 
        m = 1
        for l in arr:
            m = max(sum(l),m)
        return m
            
                
        
        