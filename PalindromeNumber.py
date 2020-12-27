class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        
        if temp<0:
            return False
        elif temp>= 0 and temp<10:
            return True
        
        res = 0
        while temp != 0:
            
            pop = self.mod(temp)
            temp = self.divide(temp)
            
            
            res = res*10 + pop
            
        if res == x:
            return True
        else:
            return False
            
            
            
            
            
    def divide(self,number):
        return int(number/10)
    def mod(self,number):
        return number%10
        