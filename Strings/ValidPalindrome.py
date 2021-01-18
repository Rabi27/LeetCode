'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        s = s.lower()
        
        while left <= right:
            
            #If the left character is not alphanumeric, we simply skip it
            #This can be done via justing incrementing the left index
            #while loop is used so to skip multiple consective characters that
            #are not alphanumeric. Same is the case is for right characters.
            while left < right and s[left].isalnum() == False: 
                left +=1
            while left < right and s[right].isalnum() == False: 
                right -=1
            
            #We are using a two pointer approach
            #left and right are the two pointers
            #when the characters at left and right are not equal we simply return False
            #String will not be a palindrome
            if s[left] != s[right]: return False
            
            left += 1
            right -= 1
            
        return True
        