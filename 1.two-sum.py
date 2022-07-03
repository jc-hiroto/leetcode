#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (48.53%)
# Likes:    34142
# Dislikes: 1076
# Total Accepted:    7M
# Total Submissions: 14.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left, right = 0, len(nums) - 1
        # sorted_nums = []
        # for i, num in enumerate(nums):
        #     sorted_nums.append([num, i])
        # sorted_nums.sort()
        # while left < right:
        #     if sorted_nums[left][0] + sorted_nums[right][0] < target:
        #         left += 1
        #     elif sorted_nums[left][0] + sorted_nums[right][0] > target:
        #         right -= 1
        #     else:
        #         break
        # return [sorted_nums[left][1], sorted_nums[right][1]]

        d = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in d:
                return [d[remain], i]
            else:
                d[num] = i
# @lc code=end
