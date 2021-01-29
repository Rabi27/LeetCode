'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #If the last digit is less than 9, then simply increment it and
        #return the digits array
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        #If the last digit is 9, then this snippet of code executes
        l = len(digits)-1
        carry = 0

        while l >= 0:
            carry = 0
            temp = digits[l] + 1
            digits[l] = temp%10 + carry
            carry = temp//10
            l -= 1
            #whenever the next digit is not 9
            #simply add one to the next digit and return the digits array
            if l>=0 and digits[l] < 9:
                digits[l] += 1
                return digits
        
        #this is a special case to handle all elements being 9
        #say the array was [9,9,9] .... the output should be [1,0,0,0]
        #the below snippet of code adds the value of carry at the index 0
        #hence the output is accurate
        digits.insert(0,carry)
        return digits

       
            
            
            
            
            
            
        
        
        
        
            
        
        
    