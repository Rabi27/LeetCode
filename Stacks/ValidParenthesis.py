'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1-Open brackets must be closed by the same type of brackets.
2-Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

'''
class Solution(object):
    def isValid(self, s):
        stack = []
        #
        for char in s:
            
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' and stack != [] and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack != [] and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack != [] and stack[-1] == '[':
                stack.pop()
            else:
                return False
            
        if stack == []:
            return True