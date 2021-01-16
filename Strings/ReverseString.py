'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''


'''
Recursive Approach

Here is an example. Let's implement recursive function helper which receives two pointers, left and right, as arguments.

Base case: if left >= right, do nothing.

Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1).

To solve the problem, call helper function passing the head and tail indexes as arguments: return helper(0, len(s) - 1).

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def helper(left,right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                helper(left+1,right-1)
                
        helper(0,len(s)-1)
        
        