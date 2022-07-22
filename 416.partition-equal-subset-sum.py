#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (46.39%)
# Likes:    8115
# Dislikes: 128
# Total Accepted:    481K
# Total Submissions: 1M
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in
# both subsets is equal.
#
#
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
#
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(sum, i):
            if sum == 0:
                return True
            if i >= len(nums) or sum < 0:
                return False
            return dp(sum - nums[i], i + 1) or dp(sum, i + 1)
        total = sum(nums)
        if total % 2 != 0:
            return False
        return dp(total // 2, 0)
# @lc code=end
