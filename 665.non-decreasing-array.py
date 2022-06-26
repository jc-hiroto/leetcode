#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (21.54%)
# Likes:    4450
# Dislikes: 694
# Total Accepted:    201.1K
# Total Submissions: 876.9K
# Testcase Example:  '[4,2,3]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.
# 
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def checkPossibility(self, N: List[int]) -> bool:
        err = 0
        for i in range(1, len(N)):
            if N[i] < N[i-1]:
                if err or (1 < i  < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
                    return False
                err = 1
        return True
# @lc code=end

