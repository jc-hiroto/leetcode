#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.24%)
# Likes:    14146
# Dislikes: 442
# Total Accepted:    817.2K
# Total Submissions: 1.8M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pref_sum = 0
        d = {0: 1}
        for num in nums:
            pref_sum += num
            if pref_sum - k in d:
                res = res + d[pref_sum - k]
            if pref_sum not in d:
                d[pref_sum] = 1
            else:
                d[pref_sum] += 1
        return res
# @lc code=end
