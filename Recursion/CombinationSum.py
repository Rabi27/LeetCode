class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if target == 0:
            return [[]]
        if target < 0:
            return False
    
        res = []
        
        for num in candidates:
            remainder = target - num
            returnedValue = self.combinationSum(candidates,remainder)
            if returnedValue != False:
                combinations = returnedValue
                for c in combinations:
                    c.insert(0,num)
                    if sorted(c) not in res:
                        res.append(sorted(c))
        
        return res
            
            
        
        
        