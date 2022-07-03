/*
 * @lc app=leetcode id=424 lang=cpp
 *
 * [424] Longest Repeating Character Replacement
 *
 * https://leetcode.com/problems/longest-repeating-character-replacement/description/
 *
 * algorithms
 * Medium (50.82%)
 * Likes:    4971
 * Dislikes: 200
 * Total Accepted:    254.2K
 * Total Submissions: 497.5K
 * Testcase Example:  '"ABAB"\n2'
 *
 * You are given a string s and an integer k. You can choose any character of
 * the string and change it to any other uppercase English character. You can
 * perform this operation at most k times.
 *
 * Return the length of the longest substring containing the same letter you
 * can get after performing the above operations.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "ABAB", k = 2
 * Output: 4
 * Explanation: Replace the two 'A's with two 'B's or vice versa.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "AABABBA", k = 1
 * Output: 4
 * Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
 * The substring "BBBB" has the longest repeating letters, which is 4.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of only uppercase English letters.
 * 0 <= k <= s.length
 *
 *
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
   public:
    int characterReplacement(string s, int k) {
        vector<int> mapping(26, 0);
        int max_len = 0, res = 0;
        for (int i = 0; i < s.size(); i++) {
            max_len = max(max_len, ++mapping[s[i] - 'A']);
            if (res - max_len < k) {
                res++;
            } else {
                mapping[s[i - res] - 'A']--;
            }
        }
        return res;
    }
};
// @lc code=end
