#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.68%)
# Likes:    10793
# Dislikes: 467
# Total Accepted:    749.2K
# Total Submissions: 1.5M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc code=start
from heapq import heapify, heappop


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        heapify(nums)
        dp = [0] * len(nums)
        start, dp[0], dp_idx = 0, 1, 1
        last = heappop(nums)
        while nums:
            num = heappop(nums)
            if num == last:
                continue
            if num - last == 1:
                dp[dp_idx] = dp_idx - start + 1
            else:
                start = dp_idx
            dp_idx += 1
            last = num
        return max(dp)


# @lc code=end
