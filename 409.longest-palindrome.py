#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (53.57%)
# Likes:    2907
# Dislikes: 165
# Total Accepted:    294.2K
# Total Submissions: 545.3K
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
# 
# 
# Example 1:
# 
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = defaultdict(int)
        res = 0
        for c in s:
            mapping[c] += 1
        for c in mapping:
            if mapping[c] % 2 == 0:
                res += mapping[c]
                mapping[c] == 0
            elif mapping[c] > 2:
                res += mapping[c] - 1
                mapping[c] = 1
        res += 1 in mapping.values()
        return res
# @lc code=end

