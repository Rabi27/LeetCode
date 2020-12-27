class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #Numbers less than 0 or ending with a 0 can never be palindrome number
        if x<0 or (x%10 == 0 and x!= 0):
            return False
       
        
        res = 0
        
        '''

        Even Number
        1212 
        res = 12
        x = 12
        loop terminates

        
        Odd Number
        12312
        x = 123
        res = 12
        loop terminates

        Loop executes until x>res .... that is when the mid of the number is reached



        '''


        while x>res:
            res = res*10 + x%10
            x = int(x/10)
            
        return x == res or x == int(res/10)
        
        
            
       
            
        
       