#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (34.08%)
# Likes:    17133
# Dislikes: 2063
# Total Accepted:    1.4M
# Total Submissions: 4.2M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
import collections


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        q1 = collections.deque(nums1)
        q2 = collections.deque(nums2)
        com = []
        while q1 and q2:
            if q1[0] < q2[0]:
                com.append(q1.popleft())
            else:
                com.append(q2.popleft())
        if q1:
            com += q1
        if q2:
            com += q2
        return com[len(com)//2] if len(com)%2 else (com[len(com)//2] + com[len(com)//2 -1])/2
        
                
# @lc code=end

