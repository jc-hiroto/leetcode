#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (63.44%)
# Likes:    9981
# Dislikes: 524
# Total Accepted:    1.4M
# Total Submissions: 2.2M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
# 
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
# 
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
from heapq import nlargest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]

        
        
# @lc code=end

