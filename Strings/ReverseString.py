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
Two Pointers Approach

In this approach, two pointers are used to process two array elements at the same time. Usual implementation is to set one pointer in the beginning and one at the end and then to move them until they both meet.

Sometimes one needs to generalize this approach in order to use three pointers, like for classical Sort Colors problem.

Algorithm

Set pointer left at index 0, and pointer right at index n - 1, where n is a number of elements in the array.

While left < right:

Swap s[left] and s[right].

Move left pointer one step right, and right pointer one step left.


'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left,right = 0,len(s)-1
        
        while left<right:
            
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
            
        s