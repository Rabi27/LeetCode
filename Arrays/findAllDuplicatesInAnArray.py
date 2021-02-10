class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dic = collections.Counter(nums)
        ans = []
        for k,v in dic.items(): 
            if v == 2:
                ans.append(k)
        return ans
        