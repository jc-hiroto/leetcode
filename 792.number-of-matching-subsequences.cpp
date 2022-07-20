/*
 * @lc app=leetcode id=792 lang=cpp
 *
 * [792] Number of Matching Subsequences
 *
 * https://leetcode.com/problems/number-of-matching-subsequences/description/
 *
 * algorithms
 * Medium (50.51%)
 * Likes:    3012
 * Dislikes: 152
 * Total Accepted:    134.8K
 * Total Submissions: 266.2K
 * Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
 *
 * Given a string s and an array of strings words, return the number of
 * words[i] that is a subsequence of s.
 *
 * A subsequence of a string is a new string generated from the original string
 * with some characters (can be none) deleted without changing the relative
 * order of the remaining characters.
 *
 *
 * For example, "ace" is a subsequence of "abcde".
 *
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcde", words = ["a","bb","acd","ace"]
 * Output: 3
 * Explanation: There are three strings in words that are a subsequence of s:
 * "a", "acd", "ace".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
 * Output: 2
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * 1 <= words.length <= 5000
 * 1 <= words[i].length <= 50
 * s and words[i] consist of only lowercase English letters.
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int numMatchingSubseq(string s, vector<string>& words) {
        int res = 0;
        vector<vector<string>> dp(26);
        for (string word : words) {
            int idx = word[0] - 'a';
            dp[idx].push_back(word);
        }
        for (char ch : s) {
            int idx = ch - 'a';
            vector<string> tmp = dp[idx];
            dp[idx].clear();
            for (string word : tmp) {
                if (word.size() == 1) {
                    res++;
                } else {
                    dp[word[1] - 'a'].push_back(word.substr(1));
                }
            }
        }
        return res;
    }
};
// @lc code=end
