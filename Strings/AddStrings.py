'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if not num1:
            return num2
        if not num2:
            return num1
        
        
        pA = len(num1)-1
        pB = len(num2)-1
        carry = 0
        s = 0
        res = []
        while pA >= 0 and pB >= 0:
            #Getting the numbers via the ord function and subtracting with 
            #ord('0') that returns the ASCII of 0.
            numA = ord(num1[pA]) - ord('0')
            numB = ord(num2[pB]) - ord('0')
            s = numA + numB + carry
            res.insert(0,str(s%10))
            carry = s//10

            pA -= 1
            pB -= 1
        
        #If there are remaining characters of num1
        while pA >= 0:
            numA = ord(num1[pA]) - ord('0')
            s = numA + carry
            res.insert(0,str(s%10))
            carry = s//10
            pA -= 1
        #If there are remaining characters of num2
        while pB >= 0:
            numB = ord(num2[pB]) - ord('0')
            s = numB + carry
            res.insert(0,str(s%10))
            carry = s//10
            pB -= 1

        #if carry has a value, add it to the front
        if carry:
            res.insert(0,str(carry))

        return ''.join(res)







        