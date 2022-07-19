/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (33.04%)
 * Likes:    25434
 * Dislikes: 1103
 * Total Accepted:    3.4M
 * Total Submissions: 10.3M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not
 * a substring.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 5 * 10^4
 * s consists of English letters, digits, symbols and spaces.
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> used;
        int start = 0, res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (used.find(s[i]) != used.end()) {
                start = max(start, used[s[i]] + 1);
            }
            used[s[i]] = i;
            res = max(res, i - start + 1);
        }
        return res;
    }
};
// @lc code=end
