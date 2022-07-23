/*
 * @lc app=leetcode id=227 lang=cpp
 *
 * [227] Basic Calculator II
 *
 * https://leetcode.com/problems/basic-calculator-ii/description/
 *
 * algorithms
 * Medium (41.58%)
 * Likes:    4597
 * Dislikes: 594
 * Total Accepted:    450.4K
 * Total Submissions: 1.1M
 * Testcase Example:  '"3+2*2"'
 *
 * Given a string s which represents an expression, evaluate this expression
 * and return its value. 
 *
 * The integer division should truncate toward zero.
 *
 * You may assume that the given expression is always valid. All intermediate
 * results will be in the range of [-2^31, 2^31 - 1].
 *
 * Note: You are not allowed to use any built-in function which evaluates
 * strings as mathematical expressions, such as eval().
 *
 *
 * Example 1:
 * Input: s = "3+2*2"
 * Output: 7
 * Example 2:
 * Input: s = " 3/2 "
 * Output: 1
 * Example 3:
 * Input: s = " 3+5 / 2 "
 * Output: 5
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 3 * 10^5
 * s consists of integers and operators ('+', '-', '*', '/') separated by some
 * number of spaces.
 * s represents a valid expression.
 * All the integers in the expression are non-negative integers in the range
 * [0, 2^31 - 1].
 * The answer is guaranteed to fit in a 32-bit integer.
 *
 *
 */

// @lc code=start
class Solution {
   public:
    int calculate(string s) {
        if (s.length() == 0) return 0;
        stack<int> st;
        int cur = 0;
        char op = '+';
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) cur = (cur * 10) + (s[i] - '0');
            if (!isdigit(s[i]) && !iswspace(s[i]) || i == s.length() - 1) {
                if (op == '-') {
                    st.push(-cur);
                } else if (op == '+') {
                    st.push(cur);
                } else if (op == '*') {
                    int stop = st.top();
                    st.pop();
                    st.push(stop * cur);
                } else if (op == '/') {
                    int stop = st.top();
                    st.pop();
                    st.push(stop / cur);
                }
                op = s[i];
                cur = 0;
            }
        }
        int res = 0;
        while (st.size() != 0) {
            res += st.top();
            st.pop();
        }
        return res;
    }
};
// @lc code=end
