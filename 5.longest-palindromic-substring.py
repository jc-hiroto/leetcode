#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.77%)
# Likes:    18565
# Dislikes: 1088
# Total Accepted:    1.9M
# Total Submissions: 5.9M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#s

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(wd, left, right):
            while left >= 0 and right < len(wd) and wd[left] == wd[right]:
                left -= 1
                right += 1
            return wd[left+1:right]
                
        res = ""
        for i in range(len(s)):
            can = helper(s, i, i)
            if len(can) > len(res):
                res = can
            can = helper(s, i, i+1)
            if len(can) > len(res):
                res = can
        return res
# @lc code=end

