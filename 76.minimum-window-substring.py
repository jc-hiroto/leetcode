#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (38.97%)
# Likes:    11263
# Dislikes: 549
# Total Accepted:    804K
# Total Submissions: 2M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
# Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
# Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
# Constraints:
#
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#

# @lc code=start
from collections import defaultdict
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_map = collections.Counter(t)
        target_len = len(t)
        start = 0
        res = ""
        for end in range(len(s)):
            if target_map[s[end]] > 0:
                target_len -= 1

            target_map[s[end]] -= 1

            while target_len == 0:
                window_len = end - start + 1
                if not res or window_len < len(res):
                    res = s[start:end + 1]

                target_map[s[start]] += 1

                if target_map[s[start]] > 0:
                    target_len += 1
                start += 1

        return res

# @lc code=end
