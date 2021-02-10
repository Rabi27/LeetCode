class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for num in nums:
            
            if num not in ans and nums.count(num) == 2:
                ans.append(num)
        return ans
        