/*
 * @lc app=leetcode id=148 lang=cpp
 *
 * [148] Sort List
 *
 * https://leetcode.com/problems/sort-list/description/
 *
 * algorithms
 * Medium (52.07%)
 * Likes:    7512
 * Dislikes: 241
 * Total Accepted:    514.2K
 * Total Submissions: 973.6K
 * Testcase Example:  '[4,2,1,3]'
 *
 * Given the head of a linked list, return the list after sorting it in
 * ascending order.
 *
 *
 * Example 1:
 *
 *
 * Input: head = [4,2,1,3]
 * Output: [1,2,3,4]
 *
 *
 * Example 2:
 *
 *
 * Input: head = [-1,5,3,4,0]
 * Output: [-1,0,3,4,5]
 *
 *
 * Example 3:
 *
 *
 * Input: head = []
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the list is in the range [0, 5 * 10^4].
 * -10^5 <= Node.val <= 10^5
 *
 *
 *
 * Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
 * (i.e. constant space)?
 *
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
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* mid = getMid(head);
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);
        return merge(left, right);
    }
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode dum(0);
        ListNode* ptr = &dum;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                ptr->next = l1;
                l1 = l1->next;
            } else {
                ptr->next = l2;
                l2 = l2->next;
            }
            ptr = ptr->next;
        }
        if (l1)
            ptr->next = l1;
        else
            ptr->next = l2;
        return dum.next;
    }
    ListNode* getMid(ListNode* head) {
        ListNode* prevMid = NULL;
        while (head && head->next) {
            prevMid = (prevMid == NULL) ? head : prevMid->next;
            head = head->next->next;
        }
        ListNode* mid = prevMid->next;
        prevMid->next = NULL;
        return mid;
    }
};
// @lc code=end
