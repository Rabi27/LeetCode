class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        count = 0
        
        for i in range(2,n):
            num = i
            status = True
            for j in range(2,i):
                
                if num%j == 0:
                    status = False
                    break
            if status == True:
                count += 1
        
        return count
                    
        
