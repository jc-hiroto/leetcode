#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (31.28%)
# Likes:    8706
# Dislikes: 288
# Total Accepted:    522.3K
# Total Submissions: 1.6M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# 
# 
# Example 2:
# 
# 
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# 
# 
# Example 3:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    closest = stack.pop()
                    dp[i + 1] = dp[closest] + i - closest + 1
        return max(dp)

# @lc code=end

