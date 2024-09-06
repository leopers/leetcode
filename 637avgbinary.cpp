#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  vector<double> averageOfLevels(TreeNode *root) {
    if (root == nullptr)
      return {};

    vector<double> average;

    queue<TreeNode *> q = {};
    q.push(root);

    while (!q.empty()) {
      double sum = 0;
      int count = q.size();

      for (int i = 0; i < count; ++i) {
        TreeNode *curr = q.front();
        q.pop();
        sum += curr->val;

        if (curr->left != nullptr)
          q.push(curr->left);
        if (curr->right != nullptr)
          q.push(curr->right);
      }

      average.push_back(sum / count);
    }

    return average;
  }
};