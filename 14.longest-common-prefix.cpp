/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (39.39%)
 * Likes:    8841
 * Dislikes: 3149
 * Total Accepted:    1.7M
 * Total Submissions: 4.2M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 *
 * Example 1:
 *
 *
 * Input: strs = ["flower","flow","flight"]
 * Output: "fl"
 *
 *
 * Example 2:
 *
 *
 * Input: strs = ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] consists of only lowercase English letters.
 *
 *
 */

// @lc code=start
class Solution {
   public:
    string longestCommonPrefix(vector<string>& strs) {
        int min_len = INT_MAX;
        for (auto s : strs) {
            min_len = min(min_len, (int)s.size());
        }
        string res;
        for (int i = 0; i < min_len; i++) {
            char c = strs[0][i];
            for (auto s : strs) {
                if (s[i] != c) {
                    return res;
                }
            }
            res += c;
        }
        return res;
    }
};
// @lc code=end
