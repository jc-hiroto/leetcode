#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (33.55%)
# Likes:    2418
# Dislikes: 42
# Total Accepted:    64.3K
# Total Submissions: 183K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# You are given an integer array nums and an integer x. In one operation, you
# can either remove the leftmost or the rightmost element from the array nums
# and subtract its value from x. Note that this modifies the array for future
# operations.
# 
# Return the minimum number of operations to reduce x to exactly 0 if it is
# possible, otherwise, return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to
# reduce x to zero.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and
# the first two elements (5 operations in total) to reduce x to zero.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        start = 0
        cur_sum = 0
        max_len = 0
        found = False
        tar = sum(nums) - x
        n = len(nums)
        for i in range(n):
            cur_sum += nums[i]
            while start <= i and cur_sum > tar:
                cur_sum -= nums[start]
                start += 1
            if cur_sum == tar:
                found = True
                max_len = max(max_len, i - start + 1)
        return len(nums) - max_len if found else -1
            
            

        
# @lc code=end

