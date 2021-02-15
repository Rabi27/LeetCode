'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for i in range(len(s)):
            
            if s.count(s[i]) == 1:
                return i
        
        return -1
        
