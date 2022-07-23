/*
 * @lc app=leetcode id=315 lang=cpp
 *
 * [315] Count of Smaller Numbers After Self
 *
 * https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
 *
 * algorithms
 * Hard (42.05%)
 * Likes:    6581
 * Dislikes: 183
 * Total Accepted:    250.3K
 * Total Submissions: 590.8K
 * Testcase Example:  '[5,2,6,1]'
 *
 * You are given an integer array nums and you have to return a new counts
 * array. The counts array has the property where counts[i] is the number of
 * smaller elements to the right of nums[i].
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [5,2,6,1]
 * Output: [2,1,1,0]
 * Explanation:
 * To the right of 5 there are 2 smaller elements (2 and 1).
 * To the right of 2 there is only 1 smaller element (1).
 * To the right of 6 there is 1 smaller element (1).
 * To the right of 1 there is 0 smaller element.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-1]
 * Output: [0]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [-1,-1]
 * Output: [0,0]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 *
 *
 */

// @lc code=start
class Solution {
   public:
    void merge(vector<pair<int, int>> &v, vector<int> &count, int left, int mid,
               int right) {
        vector<pair<int, int>> temp(right - left + 1);
        int i = left, j = mid + 1, k = 0;
        while (i <= mid && j <= right) {
            if (v[i].first <= v[j].first) {
                temp[k++] = v[j++];
            } else {
                count[v[i].second] += right - j + 1;
                temp[k++] = v[i++];
            }
        }
        while (i <= mid) {
            temp[k++] = v[i++];
        }
        while (j <= right) {
            temp[k++] = v[j++];
        }
        for (int i = left; i <= right; i++) {
            v[i] = temp[i - left];
        }
    }
    void mergeSort(vector<pair<int, int>> &v, vector<int> &count, int left,
                   int right) {
        if (left >= right) return;
        int mid = (left + right) / 2;
        mergeSort(v, count, left, mid);
        mergeSort(v, count, mid + 1, right);
        merge(v, count, left, mid, right);
    }
    vector<int> countSmaller(vector<int> &nums) {
        vector<pair<int, int>> v(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            v[i] = make_pair(nums[i], i);
        }
        vector<int> count(nums.size(), 0);
        mergeSort(v, count, 0, nums.size() - 1);
        return count;
    }
};
// @lc code=end
