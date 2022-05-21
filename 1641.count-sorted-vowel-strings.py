#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#
# https://leetcode.com/problems/count-sorted-vowel-strings/description/
#
# algorithms
# Medium (74.88%)
# Likes:    2781
# Dislikes: 62
# Total Accepted:    129.9K
# Total Submissions: 167.5K
# Testcase Example:  '1'
#
# Given an integer n, return the number of strings of length n that consist
# only of vowels (a, e, i, o, u) and are lexicographically sorted.
# 
# A string s is lexicographically sorted if for all valid i, s[i] is the same
# as or comes before s[i+1] in the alphabet.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are
# ["a","e","i","o","u"].
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the
# alphabet.
# 
# 
# Example 3:
# 
# 
# Input: n = 33
# Output: 66045
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 50 
# 
# 
#

# @lc code=start
import itertools


class Solution:
    # easy sol but slow.
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        prds = list(itertools.combinations_with_replacement(vowels, n))
        # print(prds)
        return len(prds)
# @lc code=end

