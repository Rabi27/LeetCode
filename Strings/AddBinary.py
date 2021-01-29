class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #int method takes two arguments
        #1st being the number that is to be converted to integer
        #2nd argument is the optional argument which is to specify the base 
        #of the number. Default value of base is set to 10
        #We are specifying the int method in the below example
        #to convert the string to integer form but by providing the base
        #argument, we are telling the int method to interpret the number to be
        #converted as a binary number
        #Say a = '101' ... int(a,2) will give output of 5.
        #Interpreting a as a binary and converting it to its 
        #decimal equivalent
        s = int(a,2) + int(b,2)
        
        #we are skipping the first 2 indexes because that are '0b'
        #which was not required in the solution
        return bin(s)[2:]
        