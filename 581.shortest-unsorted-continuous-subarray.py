#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (34.17%)
# Likes:    6411
# Dislikes: 228
# Total Accepted:    267.2K
# Total Submissions: 743K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array nums, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order.
# 
# Return the shortest such subarray and output its length.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4]
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: nums = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: Can you solve it in O(n) time complexity?
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_original = nums.copy()
        nums.sort()
        if nums == nums_original:
            return 0
        start = None
        end = None
        for i in range(len(nums)):
            num = nums[i]
            o_num = nums_original[i]
            if start is None and num != o_num:
                start = i
            if start is not None and num != o_num:
                end = i
        return end - start + 1
        
        # for i, (ori, new) in enumerate(zip(nums_original, nums)):
        #     if start is None and ori != new:
        #         start = i
        #     if start is not None and ori == new:
        #         end = i
        return end - start
        
# @lc code=end

