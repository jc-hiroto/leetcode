#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#
# https://leetcode.com/problems/maximum-erasure-value/description/
#
# algorithms
# Medium (52.43%)
# Likes:    1645
# Dislikes: 26
# Total Accepted:    71.3K
# Total Submissions: 125.8K
# Testcase Example:  '[4,2,4,5,6]'
#
# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is
# equal to the sum of its elements.
# 
# Return the maximum score you can get by erasing exactly one subarray.
# 
# An array b is called to be a subarray of a if it forms a contiguous
# subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some
# (l,r).
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        start = 0
        max_val = -1
        for i, num in enumerate(nums):
            # print(start, " ", max_val)
            if num in seen and seen[num] >= start:
                start = seen[num] + 1
            else:
                max_val = max(max_val, sum(nums[start:i+1]))
            seen[num] = i
        return max_val
        
# @lc code=end

