class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        temp = x
        
        if temp < 0:
            return False
        
        res = 0
        
        while temp:
            res = res*10 + temp%10
            temp = int(temp/10)
            
        return res == x
            
        
       