#include <bits/stdc++.h>
using namespace std;

// Definition for a binary tree node
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
    queue<TreeNode *> q;
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

// Helper function to print vectors for validation
void printVector(const vector<double> &vec) {
  for (double num : vec) {
    cout << num << " ";
  }
  cout << endl;
}

// Test function
void testAverageOfLevels() {
  Solution sol;

  // Test case 1: Simple binary tree
  TreeNode *root1 = new TreeNode(3);
  root1->left = new TreeNode(9);
  root1->right = new TreeNode(20);
  root1->right->left = new TreeNode(15);
  root1->right->right = new TreeNode(7);

  vector<double> expected1 = {3.0, 14.5, 11.0};
  vector<double> result1 = sol.averageOfLevels(root1);
  assert(result1 == expected1);
  cout << "Test case 1 passed!" << endl;
  printVector(result1);

  // Test case 2: Tree with only one node
  TreeNode *root2 = new TreeNode(5);
  vector<double> expected2 = {5.0};
  vector<double> result2 = sol.averageOfLevels(root2);
  assert(result2 == expected2);
  cout << "Test case 2 passed!" << endl;
  printVector(result2);

  // Test case 3: More complex binary tree
  TreeNode *root3 = new TreeNode(1);
  root3->left = new TreeNode(2);
  root3->right = new TreeNode(3);
  root3->left->left = new TreeNode(4);
  root3->left->right = new TreeNode(5);
  root3->right->left = new TreeNode(6);
  root3->right->right = new TreeNode(7);

  vector<double> expected3 = {1.0, 2.5, 5.5};
  vector<double> result3 = sol.averageOfLevels(root3);
  assert(result3 == expected3);
  cout << "Test case 3 passed!" << endl;
  printVector(result3);
}

int main() {
  testAverageOfLevels();
  return 0;
}