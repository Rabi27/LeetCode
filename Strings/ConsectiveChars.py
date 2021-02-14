'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
'''

class Solution:
    def maxPower(self, s: str) -> int:
        
        maxcount = 1
        i = 0
        size = len(s)
        
        while i < size-1:
            count = 1
            while i < size-1 and s[i] == s[i+1]:
                count += 1
                i += 1
            
            if count > maxcount:
                maxcount = count
            
            i += 1
            
        
        return maxcount
        