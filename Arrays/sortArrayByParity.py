'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        #You cannot assign to a list like lst[i] = something, 
        #unless the list already is initialized with at least i+1 elements
        
        '''
        l = [None] * 10
        l will be like,
        [None, None, None, None, None, None, None, None, None, None]
        '''
        
        res = [None]*len(A)
        
        i = 0
        for num in A:
            if num%2 == 0:
                res[i] = num
                i += 2
                
        i = 1     
        for num in A:
            if num%2 != 0:
                res[i] = num
                i += 2
        
        return res
        
                
        
