'''
Given a string s, find the length of the longest substring
without repeating characters.

'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substr = ""
        ans = []
        arr = []
        for i in range(len(s)):
            if s[i] not in substr:
                substr = substr+s[i]
            else:
                ans.append(len(substr))
                arr.append(substr)
                ind = substr.index(s[i])
                substr = substr[ind+1:]
                substr = substr+s[i]

        arr.append(substr)
        ans.append(len(substr))

        return max(ans) 
        


        