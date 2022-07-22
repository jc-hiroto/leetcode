#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (47.06%)
# Likes:    6351
# Dislikes: 323
# Total Accepted:    839.7K
# Total Submissions: 1.8M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return target
                if abs(current_sum - target) < abs(res - target):
                    res = current_sum
                if target > nums[i]+2*nums[right]:
                    break
                if target < nums[i]+2*nums[left]:
                    break
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return res

# @lc code=end
