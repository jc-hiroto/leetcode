#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (54.09%)
# Likes:    5617
# Dislikes: 98
# Total Accepted:    645.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res


    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], res)
# @lc code=end

