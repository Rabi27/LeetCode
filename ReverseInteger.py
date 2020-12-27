class Solution:
    def reverse(self, x: int) -> int:
        
        '''
        123
        
        123%10 = 3
        123/10 = 12
        
        12%10 = 2
        12/10 = 1
        
        
        res
        3*10 = 30
        30+2 = 32
        32*10 = 320
        320+1 = 321
        
        '''
        MAX_INT = 2**31-1 #= 2147483647
        MIN_INT = -2**31  #= -2147483648
        res = 0
        while x != 0:

            pop = self.mod(x)
            x = self.divide(x)
            #res >= divide(MAX_INT) == 214748364 and pop value is greater than 7
            #then by the below if statement we are preventing are overflow.
            #same case goes for the 2nd if statement
            ''''
            if res >= self.divide(MAX_INT) and pop > 7:
                return 0
            if res <= self.divide(MIN_INT) and pop < -8:
                return 0
                '''
            res = res*10 + pop
            
            
        #This is not a good solution from interview point of view.
        #Overflow has occured and then we're checking the result value.
        #A suitable solution would be to prevent an overflow from occurring
       
        if res > MAX_INT or res < MIN_INT:
            return 0
        
        return res
         
    def mod(self,number):
        if number<0:
            return number%-10
        return number%10
    
    def divide(self,number):
        return int(number/10)
    
   