#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
#
# algorithms
# Medium (55.47%)
# Likes:    1073
# Dislikes: 147
# Total Accepted:    61.5K
# Total Submissions: 110.8K
# Testcase Example:  '[5,3,2,4]'
#
# You are given an integer array nums. In one move, you can choose one element
# of nums and change it by any value.
# 
# Return the minimum difference between the largest and smallest value of nums
# after performing at most three moves.
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: Change the array [5,3,2,4] to [2,2,2,2].
# The difference between the maximum and minimum is 2-2 = 0.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,5,0,10,14]
# Output: 1
# Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
# The difference between the maximum and minimum is 1-0 = 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])
        
# @lc code=end

