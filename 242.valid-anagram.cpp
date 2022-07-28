/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (61.42%)
 * Likes:    5994
 * Dislikes: 232
 * Total Accepted:    1.5M
 * Total Submissions: 2.4M
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t, return true if t is an anagram of s, and false
 * otherwise.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 *
 *
 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, t.length <= 5 * 10^4
 * s and t consist of lowercase English letters.
 *
 *
 *
 * Follow up: What if the inputs contain Unicode characters? How would you
 * adapt your solution to such a case?
 *
 */

// @lc code=start
class Solution {
   public:
    bool isAnagram(string s, string t) {
        unordered_map<int, int> s_cnt, t_cnt;
        for (int i = 0; i < s.size(); i++) {
            s_cnt[s[i] - 'a']++;
        }
        for (int i = 0; i < t.size(); i++) {
            t_cnt[t[i] - 'a']++;
        }
        return s_cnt == t_cnt;
    }
};
// @lc code=end
