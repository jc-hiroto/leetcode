#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (28.23%)
# Likes:    8404
# Dislikes: 1278
# Total Accepted:    697.7K
# Total Submissions: 2.5M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start
class Solution:
    # Recursion solution
    # More version of sol: https://leetcode.com/problems/regular-expression-matching/solution/
    def isMatch(self, S: str, R: str) -> bool:
        if not R:
            return not S
        match = bool(S) and R[0] in {S[0], "."}
        if len(R) >= 2 and R[1] == "*":
            return self.isMatch(S, R[2:]) or match and self.isMatch(S[1:], R)
        else:
            return match and self.isMatch(S[1:], R[1:])
# @lc code=end

