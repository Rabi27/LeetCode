class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def check(nums,target):
            if target in memo: return memo[target]
            if target == 0:
                return 1
            if target < 0:
                return 0

            count = 0

            for num in nums:
                remainder = target - num
                totalCount = check(nums,remainder)
                count += totalCount
            
            memo[target] = count
            return count
        
        return check(nums,target)