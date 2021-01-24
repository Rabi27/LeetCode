'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
 

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        
        power = 1
        ans = 0
        l = len(s)-1
        #we are substracting with 64, so as to get ascii value of the alphabet
        #i.e when A - 64 is done, we get 1
        #ascii of A is 65
        #The ord function in Python is used to get ASCII of character
        #this function takes a string of length 1 as arguemnt ... a single character
        while l>= 0:
            
            ans = ans + power*(ord(s[l])-64)
            l -= 1
            power = power*26
            
        return ans
        