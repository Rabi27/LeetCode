'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000


'''

import math

class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        l = sorted(nums1 + nums2)
        if len(l)%2 == 0:
            n = len(l)//2
            return float((l[n]+l[n-1])/float(2))
        else:
            return l[len(l)//2]