/*
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 *
 * https://leetcode.com/problems/backspace-string-compare/description/
 *
 * algorithms
 * Easy (47.25%)
 * Likes:    3904
 * Dislikes: 190
 * Total Accepted:    415.9K
 * Total Submissions: 878.5K
 * Testcase Example:  '"ab#c"\n"ad#c"'
 *
 * Given two strings s and t, return true if they are equal when both are typed
 * into empty text editors. '#' means a backspace character.
 *
 * Note that after backspacing an empty text, the text will continue empty.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "ab#c", t = "ad#c"
 * Output: true
 * Explanation: Both s and t become "ac".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "ab##", t = "c#d#"
 * Output: true
 * Explanation: Both s and t become "".
 *
 *
 * Example 3:
 *
 *
 * Input: s = "a#c", t = "b"
 * Output: false
 * Explanation: s becomes "c" while t becomes "b".
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, t.length <= 200
 * s and t only contain lowercase letters and '#' characters.
 *
 *
 *
 * Follow up: Can you solve it in O(n) time and O(1) space?
 *
 */

// @lc code=start
#include <stack>
class Solution {
   public:
    bool backspaceCompare(string s, string t) {
        stack<char> st1, st2;
        for (char c : s) {
            if (c == '#') {
                if (!st1.empty()) st1.pop();
            } else {
                st1.push(c);
            }
        }
        for (char c : t) {
            if (c == '#') {
                if (!st2.empty()) st2.pop();
            } else {
                st2.push(c);
            }
        }
        while (!st1.empty() && !st2.empty()) {
            if (st1.top() != st2.top() || st1 != st2) return false;
            st1.pop();
            st2.pop();
        }
        return st1.empty() && st2.empty();
    }
};
// @lc code=end
