/*
 * @lc app=leetcode id=234 lang=cpp
 *
 * [234] Palindrome Linked List
 *
 * https://leetcode.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (46.58%)
 * Likes:    9621
 * Dislikes: 586
 * Total Accepted:    1M
 * Total Submissions: 2.2M
 * Testcase Example:  '[1,2,2,1]'
 *
 * Given the head of a singly linked list, return true if it is a
 * palindrome.
 *
 *
 * Example 1:
 *
 *
 * Input: head = [1,2,2,1]
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: head = [1,2]
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the list is in the range [1, 10^5].
 * 0 <= Node.val <= 9
 *
 *
 *
 * Follow up: Could you do it in O(n) time and O(1) space?
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
   public:
    bool isPalindrome(ListNode* head) {
        ListNode *slow = head, *fast = head, *rev = nullptr;
        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            rev = new ListNode(slow->val, rev);
            slow = slow->next;
        }
        if (fast != nullptr) slow = slow->next;
        while (rev != nullptr && rev->val == slow->val) {
            slow = slow->next;
            rev = rev->next;
        }
        return rev == nullptr;
    }
};
// @lc code=end
